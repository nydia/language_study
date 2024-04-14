"""
用户的封装，用户权限校验
"""
from files.utils.cache import memory_cache
from files.utils.log_utils import log_util

uname = 'nydia'
upass = 'nydia#qaz'
# 用户名密码内存过期时间
timeout_val = 10

def init_user():
    # memory_cache.set_value(uname, upass, 6)  # 设置一个 6 秒过期的键值对
    memory_cache.set_value(uname, upass, timeout_val)
def check_user():
    log_util.info("检查用户>>>>")
    memory_cache.check_key(uname)
    
def user_login(uname, upass):
    log_util.info("用户登录>>>> login params : " + uname + ", " + upass)
    