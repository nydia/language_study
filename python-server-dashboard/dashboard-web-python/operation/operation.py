#-*- coding:utf-8 -*-
from config.config_api import DashboardConfig
from machine.machine import MachineApi
from utils.log_utils import LogUtils
from utils.str_utils import StrUtils
from Crypto.Cipher import AES
import base64
import codecs

"""
常用运维操作
"""
class CommonOpt:
    def __init__(self) -> None:
        pass
    """
    删除对账数据 (类方法：直接 CommonOpt.del_soa_date)
    """
    @classmethod
    def del_soa_date(cls,envi,soa_dt,uname,passwd,channel):
        LogUtils().info(">>>>>>删除对账数据参数: [env={},date={},uname={},passwd={},channel={}]",envi,soa_dt,uname,passwd,channel)

        _result = ""
        _machine_api = MachineApi()
        _config = DashboardConfig().get_config()

        _command = "/opt/appl/spring-cloud/gold-soa-data-delete.sh {} {} {} {} {}".format(envi,uname,passwd,soa_dt,channel)
        _exec_result = _machine_api.shell_execute(
            _config['operation']['del_soa_shell_host'],
            _config['machine']['sit']['user'],
            _config['machine']['sit']['pass'],
            _command
        )

        if _exec_result is not None and len(_exec_result) > 0:
            for _line in _exec_result:
                if StrUtils.is_not_blank(_line) and StrUtils.to_str(_line).startswith("execute_result:"):
                    _result = StrUtils.substr(StrUtils.to_str(_line),StrUtils.to_str(_line).index("execute_result:") + 15,None)
                    # 获取到的服务执行结果: "code":"000000","data":"success","message":"处理成功"}
        
        LogUtils().info("获取到的服务执行结果: {}", _result)        
        return _result

    """
    获取SIT环境发布服务的状态
    """
    @classmethod
    def get_sit_web_deploy_status(cls):
        LogUtils().info(">>>>>>获取SIT环境发布服务的状态")

        _result = ""
        _machine_api = MachineApi()
        _config = DashboardConfig().get_config()

        _command = "pgrep python"
        _exec_result = _machine_api.command_execute(
            _config['operation']['sit_web_deploy_host'],
            _config['machine']['sit']['user'],
            _config['machine']['sit']['pass'],
            _command
        )
        LogUtils().info("获取到的服务执行结果: {}", _exec_result)

        if StrUtils.is_not_blank(_exec_result):
            _result = "true"
        else:
            _result = "false" 
        return _result

    """
    开始启动SIT环境发布服务
    """
    @classmethod
    def start_sit_web_deploy_server(cls):
        LogUtils().info(">>>>>>开始启动SIT环境发布服务")

        _result = ""
        _machine_api = MachineApi()
        _config = DashboardConfig().get_config()

        _command = "python /home/oper/h5/start_server_v2.py & "
        _exec_result = _machine_api.command_execute(
            _config['operation']['sit_web_deploy_host'],
            _config['machine']['sit']['user'],
            _config['machine']['sit']['pass'],
            _command
        )
        LogUtils().info("获取到的服务执行结果: {}", _exec_result)
        
        _result = "true"    
        
        return _result

    """
    解密短信内容
    """
    @classmethod
    def decrypt_sms_content(cls, content):
        _config = DashboardConfig().get_config()
        aes_key = _config['operation']['sms_aes_key']
        print("key: " + aes_key)
        aes_key_encode = aes_key.encode('utf-8')
        content_encode = content.encode('utf-8')
        cipher = AES.new(aes_key_encode,AES.MODE_ECB)
        _content = cipher.decrypt(content_encode)
        print(_content)
        #print(base64.decode(_content, _c))
        #print(str(_content,'utf-8'))
        print("codes: " + codecs.decode(_content))
        return _content
    @classmethod
    def aes_decode(cls, content):
        decrypted_text = ""
        try:
            _config = DashboardConfig().get_config()
            key = _config['operation']['sms_aes_key']
            print("key-----: " +  key)
            aes = AES.new(bytes(key, encoding='utf8'), AES.MODE_ECB)  # 初始化加密器
            #decrypted_text = aes.decrypt(bytes(content, encoding='utf8')).decode("utf8")  # 解密
            decrypted_text = aes.decrypt(bytes(content, encoding='utf8'))  # 解密
            print("content--------:" + decrypted_text)
            #decrypted_text = decrypted_text[:-ord(decrypted_text[-1])]  # 去除多余补位
            print(decrypted_text)
        except Exception as e:
            pass
        return decrypted_text