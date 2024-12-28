import schedule
import time
import threading
from machine.machine import MachineApi
from jenkins_api.jenkins_api import JenkinsApi
from gitlab_api.gitlab_api import GitlabApi
from db.jenkins_job import JenkinsJobDb
from db.models import JenkinsJob
from utils.str_utils import StrUtils
from utils.log_utils import LogUtils
from config.config_api import DashboardConfig

class CommonTask:
    def __init__(self) -> None:
        pass
    def start_task(self): # 启动任务，开启线程
        # 同步机器信息
        _thread_update_machine = threading.Thread(target=self.schedule_machine_job)
        _thread_update_machine.start()

        # 同步jenkins job信息
        _thread_update_jenkins_job = threading.Thread(target=self.schedule_jenkins_job)
        _thread_update_jenkins_job.start()

        # 同步git信息
        _thread_update_project_info = threading.Thread(target=self.schedule_project_git_info)
        _thread_update_project_info.start()

        # 同步应用发布信息
        _thread_update_server_state = threading.Thread(target=self.schedule_server_state_sync)
        _thread_update_server_state.start()

    def schedule_machine_job(self): # 启动定时任务：更新机器的信息
        _machine_api = MachineApi()
        schedule.every(1800).seconds.do( _machine_api.sync_machine_info)  # 每隔 1800 秒执行一次
        while True:
            schedule.run_pending()
            time.sleep(1)

    def schedule_jenkins_job(self): # 启动定时任务：更新Jenkins Job
        schedule.every(7200).seconds.do(self.sync_jenkins_job)  # 每隔 1800 秒执行一次
        while True:
            schedule.run_pending()
            time.sleep(1)

    def schedule_project_git_info(self): # 启动定时任务：更新git 项目信息到数据库
        schedule.every(7200).seconds.do(self.sync_project_git_info)  # 每隔 3600 秒执行一次
        while True:
            schedule.run_pending()
            time.sleep(1)

    def schedule_server_state_sync(self): # 启动定时任务：更新应用服务信息
        schedule.every(3600).seconds.do(self.sync_docker_server_state)  # 每隔 3600 秒执行一次
        while True:
            schedule.run_pending()
            time.sleep(1)

    def sync_jenkins_job(self): # 同步jenkins job信息
        _jenkins_api = JenkinsApi()
        _jenkins_api.login()
        _job_list = _jenkins_api.job_list()
        LogUtils().info("获取到的jenkins的长度: {}", len(_job_list))

        _jenkins_job_db = JenkinsJobDb()
        if  _job_list is not None:   
            for job in _job_list:
                #print("获取到的jenkins名称:", job["name"])
                _job_info = _jenkins_job_db.get_job_info_by_name(job["name"])
                if _job_info is None:
                    _jenkins_job = JenkinsJob()
                    _jenkins_job.job_name = job["name"]
                    _jenkins_job_db.insert_job(_jenkins_job)

    def sync_project_git_info(self): # 同步项目的git实时信息
        _gitlab_api = GitlabApi()
        _gitlab_api.login()
        project_list_remote = _gitlab_api.get_project_list()

        _jenkins_job_db = JenkinsJobDb()
        job_list_local = _jenkins_job_db.get_job_list()

        #print("project_list_remote len > ", len(project_list_remote), " || job_list_local len > ", len(job_list_local))

        if project_list_remote is not None:
            if job_list_local is not None:
                for _job in job_list_local:
                    for _project in project_list_remote:
                        if _project.name == _job.job_name:
                            _update_job = JenkinsJob()
                            _update_job.id = _job.id
                            _update_job.project_id = _project.project_id
                            #_jenkins_job_db.update_job_git_info(_update_job)
    
    def sync_docker_server_state(self): # 同步所有的服务状态
        _machine_api = MachineApi()

        _config = DashboardConfig().get_config()

        _job_db = JenkinsJobDb()
        _list = _job_db.get_job_list()

        if _list is not None:   
            for _job in _list:
                if StrUtils.is_not_blank(_job.image_name) and _job.status == '1':
                    _state_dev = ""
                    _state_sit = ""
                    if StrUtils.is_not_blank(_job.deploy_host_dev):
                        _username = _config['machine']['dev-sh']['user']
                        _password = _config['machine']['dev-sh']['pass']
                        _state = _machine_api.get_machine_docker_server_state(_job.deploy_host_dev, _username, _password, _job.image_name)
                        if StrUtils.is_not_blank(_state):
                            LogUtils().info(">>>>>>服务[{}]状态: {}",_job.deploy_host_dev,_state)
                            #LogUtils().info("dev更新信息参数,id[{}],dev_status[{}],sit_status[{}],pit_status[{}]",_job.id,_state,_job.env_sit_status,_job.env_pit_status)
                            _state_dev = _state

                    if StrUtils.is_not_blank(_job.deploy_host_sit):
                        _username = _config['machine']['sit']['user']
                        _password = _config['machine']['sit']['pass']
                        _state = _machine_api.get_machine_docker_server_state(_job.deploy_host_sit, _username, _password, _job.image_name)
                        if StrUtils.is_not_blank(_state):
                            LogUtils().info(">>>>>>服务[{}]状态: {}",_job.deploy_host_sit,_state)
                            #LogUtils().info("sit更新信息参数,id[{}],dev_status[{}],sit_status[{}],pit_status[{}]",_job.id,_job.env_dev_status,_state,_job.env_pit_status)
                            _state_sit = _state

                    _job_update = JenkinsJob().build_server_state(
                            _job.id,
                            _state_dev,
                            _state_sit,
                            _job.env_pit_status
                    )
                    _job_db.update_job_server_state(_job_update)