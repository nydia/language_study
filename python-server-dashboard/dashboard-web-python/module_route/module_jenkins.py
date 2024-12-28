#-*- coding:utf-8 -*-
from flask import request, Blueprint,render_template
from utils.response_handle import resp_json_ok
from jenkins_api.jenkins_api import JenkinsApi
from gitlab_api.gitlab_api import GitlabApi
from db.jenkins_job import JenkinsJobDb
jenkins_opt = Blueprint('jenkins_opt', __name__)

# 进入部署页面
'''
deploy_option  部署选项, 进入项目构建详情页面, 选择构建参数
arg1: job_name   项目名称
arg2: project_id 对应git项目project_id
return2: git项目远程分支列表 
'''
@jenkins_opt.route('/deploy_option')
def deploy_option():
    job_id = request.args.get('job_id')

    _job_db = JenkinsJobDb()
    _job = _job_db.get_job_info_by_id(job_id)

    _gitlab_api = GitlabApi()
    _gitlab_api.login()
    branches = _gitlab_api.get_project_branches(project_id=_job.project_id)

    return render_template(
        'deploy.html',
        job_name=_job.job_name,
        branche_list=branches,
        deploy_host_dev=_job.deploy_host_dev,
        deploy_host_sit=_job.deploy_host_sit
    )

# 部署任务
'''
build 发起构建任务
arg1: job_name     
arg2: deploy_option  构建类型(deploy, rollback, restart)
arg3: deploy_env     发布环境(dev, sit, pit)
arg4: branche        构建分支
arg5: pit_flg        是否发布阿里云 0-否, 1-是
'''
@jenkins_opt.route('/build')
def build():
    job_name = request.args.get('job_name')
    deploy_option = request.args.get('deploy_option')
    deploy_env = request.args.get('deploy_env')
    branche = request.args.get('branche')
    pit_flg = request.args.get('pit_flg')
    #print("开始构建任务:",job_name)
    _jenkins_api = JenkinsApi()
    _jenkins_api.login()
    _jenkins_api.job_build(job_name, deploy_option, deploy_env, branche, pit_flg)
    return resp_json_ok(desc="发起任务成功",data=None),200,{"Content-Type":"application/json"}

# 构建日志
@jenkins_opt.route('/buildLog')
def buildLog():
    job_name = request.args.get('job_name')
    _jenkins_api = JenkinsApi()
    _jenkins_api.login()
    out_put,last_build_building = _jenkins_api.build_log(job_name)
    data_dict = {"out_log": out_put, "build_status": last_build_building}
    return resp_json_ok(desc="获取日志成功",data=data_dict),200,{"Content-Type":"application/json"}