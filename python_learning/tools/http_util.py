#-*- coding:utf-8 -*-
import requests
from log_utils import LogUtils
from str_utils import StrUtils

class HttpUtils:
    def __init__(self) -> None:
        pass

    @classmethod
    def get(cls,url):
        _data = ""
        try:
            # 发送一个简单的 HTTP GET 请求
            response = requests.get(url)
            # 检查是否成功获取响应
            if response.status_code == 200:
                # 获取响应内容（通常是 JSON 数据）
                _data = response.json()
                LogUtils().info(">>>>>>Get Response Data: {}", _data)
            else:
                print(f"HTTP GET Request Failed with status code: {response.status_code}")
        except Exception as e:
            LogUtils().info("GET请求失败,错误信息：{}", e)        
        return _data

    """
    post请求: 
    url: 请求url
    params: 请求参数 dict类型 包括: params_type 参数类型(form/json))  params_data 参数值
    """
    @classmethod
    def post(cls,url,params):
        try:
            # 发送 HTTP POST 请求
            if params is None:
                return None
            if StrUtils.equals("form",params['params_type']):
                head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 'Connection': 'close'}
                response = requests.post(url, data=params['params_data'], headers=head)
            else:
                response = requests.post(url, data=params['params_data'])

            # 检查是否成功获取响应
            if response.status_code == 200:
                # 获取响应内容（通常是 JSON 数据）
                _data = response.json()
                LogUtils().info("Post Response: {}", _data)
            else:
                print(f"HTTP POST Request Failed with status code: {response.status_code}")
            return _data   
        except Exception as e:
            LogUtils().info("POST请求失败,错误信息：{}", e)

    """
    获取html
    """
    @classmethod     
    def get_html(cls,url):
        try:
            _html = requests.get(url).content
            return _html
        except Exception as e:
            LogUtils().info("获取html请求失败,错误信息：{}", e)