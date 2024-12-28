#-*- coding:utf-8 -*-
from flask import request, Blueprint,render_template
from utils.response_handle import resp_json_ok
from task.task import CommonTask
task_opt = Blueprint('task_opt', __name__)

'''
进入定时任务页面
'''
@task_opt.route('/task/index', methods=['GET'])
def task_index():
    return render_template('task.html')

'''
启动定时任务
'''
@task_opt.route('/task/start', methods=['GET','POST'])
def task_start():
    # start task
    _task = CommonTask()
    _task.start_task()

    return resp_json_ok(desc="任务已经启动",data=None),200,{"Content-Type":"application/json"}