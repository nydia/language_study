"""
基于日志组件loguru封装日志方法
使用log_util即可
"""
from loguru import logger

class LogUtils:
    def __init__(self):
        pass
    def info(self, msg):
        logger.info(msg)
        
        
log_util = LogUtils()