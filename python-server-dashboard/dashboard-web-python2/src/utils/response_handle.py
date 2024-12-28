#-*- coding:utf-8 -*-

from src.config.constants import Constants
from flask import jsonify

def resp_json_ok(desc,data):

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