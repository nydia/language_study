#-*- coding:utf-8 -*-
from flask import request, render_template, Blueprint
from utils.response_handle import resp_json_ok
from ansible_api.ansible_playbook_opt import AnsiblePlaybookOpt
ansible_opt = Blueprint('ansible_opt', __name__)

# 请求的url： http://10.200.5.34:8088/ansible_opt/index
@ansible_opt.route('/index', methods=['GET'])
def cache_page():
    return render_template('server_status.html',title='服务状态首页')

# 请求的url： http://10.200.5.34:8088/ansible_opt/server_status?hostname=name
@ansible_opt.route('/server_status', methods=['GET'])
def server_status():
    _hostname = request.args.get('hostname')
    result = AnsiblePlaybookOpt.check_server_status(_hostname)
    return resp_json_ok(desc="操作成功",data=result),200,{"Content-Type":"application/json"}