#-*- coding:utf-8 -*-
from flask import Blueprint
from src.utils.response_handle import resp_json_ok
from src.ansible_api.ansible_playbook_opt import AnsiblePlaybookOpt
ansible_opt = Blueprint('ansible_opt', __name__)

# 请求的url： 
#   http://10.200.5.34:8089/ansible_opt/server_status?key=server_key
#   http://172.30.41.16:8089/ansible_opt/server_status
@ansible_opt.route('/server_status', methods=['GET'])
def server_status():
    result = AnsiblePlaybookOpt.check_server_status()
    return resp_json_ok(desc="操作成功",data=result),200,{"Content-Type":"application/json"}