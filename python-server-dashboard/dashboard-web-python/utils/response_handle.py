import json
from db.models import ResponseDTO
from utils.encoder import MyEncoder
from config.constants import Constants
from flask import jsonify

def resp_json_ok(desc,data):
    # 第一种方式：自定义编码
    #_resp = ResponseDTO(Constants.RESP_CODE_SUCCESS,Constants.RESP_DEFAULT_MSG,"")
    #_resp_json = json.dumps(_resp,cls=MyEncoder,indent=4)  # 将python的字典转换为json字符串
    #return _resp_json,200,{"Content-Type":"application/json"}

    # 返回字典
    #_resp = dict()
    #_resp['code'] = Constants.RESP_CODE_SUCCESS
    #_resp['desc'] = Constants.RESP_DEFAULT_MSG
    #_resp_json = json.dumps(_resp)
    #return _resp_json,200,{"Content-Type":"application/json"}

    # 使用flask的jsonify
    _resp = dict()
    _resp['code'] = Constants.RESP_CODE_SUCCESS
    if desc is None:
       _resp['desc'] = Constants.RESP_DEFAULT_MSG
    else:
      _resp['desc'] = desc
    if data is not None:
       _resp['data'] = data
    return jsonify(_resp)