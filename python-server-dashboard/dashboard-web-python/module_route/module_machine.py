#-*- coding:utf-8 -*-
from flask import request, Blueprint,render_template
from utils.response_handle import resp_json_ok
from utils.str_utils import StrUtils
from utils.log_utils import LogUtils
from machine.machine import MachineApi
from task.thread_pool import ThreadPool
from db.jenkins_job import JenkinsJobDb
from db.models import LoginFrom,JenkinsJob
from config.config_api import DashboardConfig
machine_opt = Blueprint('machine_opt', __name__)

# 同步部署服务器真实信息到本地数据库
'''
机器信息同步接口
'''
@machine_opt.route('/machineInfo', methods=['GET'])
def machineInfo():
    _machine_id = request.args.get('machine_id')
    _machine_api = MachineApi()
    _machine_api.get_machine_info(_machine_id)

    #return response_handle(desc="已加入自动同步进程",data=None),200,{"Content-Type":"application/json"}
    #return response_handle(desc="已加入自动同步进程",data=None),200,{"Content-Type":"application/json"}
    return resp_json_ok(desc="已加入自动同步进程",data=None),200,{"Content-Type":"application/json"}

'''
同步server状态到数据库
'''
@machine_opt.route('/get_server_info', methods=['GET'])
def getServerState():
    job_id = request.args.get('job_id')
    # 1.直接调用
    #sync_server_state(job_id)

    # 2.加入线程池
    ThreadPool().thread_start_get_docker_server_info(sync_server_state,job_id)

    return resp_json_ok(desc="已加入自动同步进程",data=None),200,{"Content-Type":"application/json"}

def sync_server_state(job_id):
    _config = DashboardConfig().get_config() # 获取配置
    _machine_api = MachineApi()
    _job_db = JenkinsJobDb()

    _job = _job_db.get_job_info_by_id(job_id) # 从db获取job信息
    if _job is not None:
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
            LogUtils().info(">>>>>>更新应用服务状态参数：{}", _job_update.__str__())

            _job_db.update_job_server_state(_job_update)