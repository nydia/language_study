#-*- coding:utf-8 -*-
from flask import request, Blueprint,render_template
from utils.response_handle import resp_json_ok
from operation.operation import CommonOpt
common_opt = Blueprint('common_opt', __name__)

"""
常用运维操作
"""

# 运维页面
@common_opt.route('/index')
def operation():
    _result = CommonOpt.get_sit_web_deploy_status()
    return render_template('operation_common.html',title='盟秀Dashboard',sit_web_deploy_status=_result)

@common_opt.route('/opt_del_soa_data')
def opt_del_soa_data():
    envi = request.args.get('envi')
    soa_date = request.args.get('soa-date')
    uname = request.args.get('uname')
    passwd = request.args.get('passwd')
    channel = request.args.get('channel')
    _result = CommonOpt.del_soa_date(envi,soa_date,uname,passwd,channel)
    return resp_json_ok(desc="数据删除成功",data=_result),200,{"Content-Type":"application/json"}

@common_opt.route('/start_sit_web_deploy_server')
def start_sit_web_deploy_server():
    _result = CommonOpt.start_sit_web_deploy_server()
    return resp_json_ok(desc="服务启动成功",data=_result),200,{"Content-Type":"application/json"}

# 解密短信内容
@common_opt.route('/decrypt_sms_content')
def decrypt_sms_content():
    
    return resp_json_ok(desc="服务启动成功",data=None),200,{"Content-Type":"application/json"}