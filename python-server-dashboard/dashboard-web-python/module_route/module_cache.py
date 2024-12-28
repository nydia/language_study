#-*- coding:utf-8 -*-
from utils.cache import cache_add,cache_get
from flask import request, Blueprint,render_template
from utils.response_handle import resp_json_ok
cache_opt = Blueprint('cache_opt', __name__)

@cache_opt.route('/index', methods=['GET'])
def cache_page():
    return render_template('operation_cache.html',title='缓存操作')

# 请求的url： http://10.200.5.34:8088/cache_opt/get?key=test_cache_2
@cache_opt.route('/get', methods=['GET'])
def get_cache():
    key = request.args.get('key')
    _value = cache_get(key, "")
    return resp_json_ok(desc="操作成功",data=_value),200,{"Content-Type":"application/json"}

# 请求的url： http://10.200.5.34:8088/cache_opt/add?key=test_cache_2&value=测试2
@cache_opt.route('/set', methods=['GET'])
def add_cache():
    key = request.args.get('key')
    value = request.args.get('val')
    print("key==" + key + ",val==" + value)
    cache_add(key,value)
    return resp_json_ok(desc="操作成功",data=None),200,{"Content-Type":"application/json"}