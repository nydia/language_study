# _*_ coding:utf-8 _*_
from flask import g,current_app
import functools
import datetime
import jwt
from jwt import exceptions
from config.constants import Constants
from config.config_api import DashboardConfig
from utils.cache import cache_get
from utils.log_utils import LogUtils

# 构造header
headers = {
    'typ': 'jwt',
    'alg': 'HS256'
}

def create_token(username, password):
    # 构造payload
    payload = {
        'username': username,
        'password': password,  # 自定义用户ID
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)  # 超时时间
    }
    result = jwt.encode(payload=payload, key=Constants.JWT_SLAT, algorithm="HS256", headers=headers)
    return result
 
 
def verify_jwt(token, secret=None):
    """
    检验jwt
    :param token: jwt
    :param secret: 密钥
    :return: dict: payload
    """
    if not secret:
        #secret = current_app.config['JWT_SECRET']
        secret = DashboardConfig().get_config()['auth']['jwt_secret']
 
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return payload
    except exceptions.ExpiredSignatureError:  # 'token已失效'
        return 1
    except jwt.DecodeError:  # 'token认证失败'
        return 2
    except jwt.InvalidTokenError:  # '非法的token'
        return 3
 
"""
python装饰器
""" 
def login_required(f):
    '让装饰器装饰的函数属性不会变 -- name属性'
    '第1种方法,使用functools模块的wraps装饰内部函数'
 
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            LogUtils().info("开始执行wrapper>>>>>>")
            if g.username == 1:
                return {'code': 4001, 'message': 'token已失效'}, 401
            elif g.username == 2:
                return {'code': 4001, 'message': 'token认证失败'}, 401
            elif g.username == 3:
                return {'code': 4001, 'message': '非法的token'}, 401
            else:
                return f(*args, **kwargs)
        except BaseException  as e:
            LogUtils().info("执行拦截错误>>>:", e)
            return {'code': 4001, 'message': '请先登录认证.'}, 401
 
    '第2种方法,在返回内部函数之前,先修改wrapper的name属性'
    # wrapper.__name__ = f.__name__
    return wrapper

# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    _token = cache_get(DashboardConfig().get_config()['auth']['token_key'])
    if _token is not None:
        resp.headers['Authorization'] = 'Bearer ' + _token

    return resp