import yaml
import os
import logging
from utils.log_utils import LogUtils

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class DashboardConfig:
    env_dev = "dev" #开发环境
    env_sit = "sit" #测试环境
    env_pit = "pit" #正式环境
    env = "dev"

    def __init__(self) -> None:
        if DashboardConfig.env == DashboardConfig.env_dev:
            self._config_file = 'dashboard-dev.yaml'
        elif DashboardConfig.env == DashboardConfig.env_sit:
            self._config_file = 'dashboard-sit.yaml'
        elif DashboardConfig.env == DashboardConfig.env_pit:
            self._config_file = 'dashboard-pit.yaml'
        else:
            print("配置环境错误......")
        pass
    def yaml_config_load(selef,file_path):
        #LogUtils().info("加载 {} 文件......",file_path)
        try:
            with open(file_path, encoding='utf-8') as f:
                _data = yaml.safe_load(f)
        except Exception as e:
            LogUtils().info("读取yaml文件错误，错误原因：{}", e)
        return _data

    def get_config(self):
        file_path = os.path.join(BASE_PATH, "config", self._config_file)
        try:
            _data = self.yaml_config_load(file_path)
        except Exception as e:
            LogUtils().info("读取yaml文件错误，错误原因：{}", e)    
        return _data

    def get_redis_nodes(self):
        _config = self.get_config()
        _nodes = _config['cache']['redis']['sentinel-nodes']
        _arr = []
        for e in _nodes:
            _arr.append(tuple(e)) # tuple数组转为元组
        return _arr