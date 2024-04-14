"""
用户的封装，用户权限校验
"""
from files.utils.cache import memory_cache
from files.utils.log_utils import log_util

uname_val = 'nydia'
upass_val = 'nydia#qaz'
# 用户名密码内存过期时间
timeout_val = 3600

def init_user():
    # memory_cache.set_value(uname, upass, 6)  # 设置一个 6 秒过期的键值对
    memory_cache.set_value(uname_val, upass_val, timeout_val)
def user_login(uname, upass):
    log_util.info("用户登录>>>> login params : {},{}".format(uname,upass))
    if uname == uname_val and upass == upass_val:
        log_util.info("登录成功>>>>>>>")
        init_user()
        return True
    else:
        log_util.info("登录失败>>>>>>>")
        return False
def check_user():
    log_util.info("检查用户>>>>")
    result = memory_cache.check_key(uname_val)
    log_util.info("检查结果：{}".format(result))
    return result
    

    