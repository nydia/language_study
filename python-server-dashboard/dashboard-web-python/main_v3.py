#-*- coding:utf-8 -*-
from flask import g, Flask, request, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap5
import jwt
from jwt import exceptions as jwt_exceptions
from db.machine_db import MachineDb
from db.jenkins_job import JenkinsJobDb
from db.models import LoginFrom
from utils.cache import cache_add,cache_get,cache_del
from utils.log_utils import LogUtils
from config.constants import Constants
from config.config_api import DashboardConfig
from auth.auth_jwt import after_request,login_required,create_token,verify_jwt
# route 模块
from module_route.module_cache import cache_opt
from module_route.module_jenkins import jenkins_opt
from module_route.module_task import task_opt
from module_route.module_common_opt import common_opt
from module_route.module_machine import machine_opt
from module_route.module_ansible import ansible_opt

app = Flask(__name__)
bootstrap=Bootstrap5(app)
# 注册蓝图，并指定其对应的前缀（url_prefix）
app.register_blueprint(cache_opt, url_prefix="/cache_opt")
app.register_blueprint(jenkins_opt, url_prefix="/jenkins_opt")
app.register_blueprint(task_opt, url_prefix="/task_opt")
app.register_blueprint(common_opt, url_prefix="/common_opt")
app.register_blueprint(machine_opt, url_prefix="/machine_opt")
app.register_blueprint(ansible_opt, url_prefix="/ansible_opt")

# 请求后处理
app.after_request(after_request)


######################  >>>>> 接口鉴权security  start <<<<<  ##########
@app.before_request
def security_authentication():
    """
    1.获取请求头Authorization中的token
    2.判断是否以 Bearer开头
    3.使用jwt模块进行校验
    4.判断校验结果,成功就提取token中的载荷信息,赋值给g对象保存
    """

    _config = DashboardConfig().get_config()
    path = request.path
    for _url in _config['auth']['no_auth_url'].split(","):
        if path == _url:
            return None

    auth = request.headers.get('Authorization')
    if auth and auth.startswith('Bearer '):
        "提取token 0-6 被Bearer和空格占用 取下标7以后的所有字符"
        token = auth[7:]
        "校验token"
        g.username = None
        try:
            "判断token的校验结果"
            payload = jwt.decode(token, Constants.JWT_SLAT, algorithms=['HS256'])
            "获取载荷中的信息赋值给g对象"
            g.username = payload.get('username')
        except jwt_exceptions.ExpiredSignatureError:  # 'token已失效'
            g.username = 1
        except jwt.DecodeError:  # 'token认证失败'
            g.username = 2
        except jwt.InvalidTokenError:  # '非法的token'
            g.username = 3
    else:
        # 临时
        _token = cache_get(DashboardConfig().get_config()['auth']['token_key'])
        _payload = verify_jwt(_token)
        LogUtils().info(" >>>_payload type: {}", _payload)
        if _payload != 1 and _payload != 2 and _payload != 3:
            return None
        return redirect("/login")
######################  >>>>> 接口鉴权security  end <<<<<  ##########


######################  >>>>> login  start <<<<<  ###################
# 登录操作  get是进入这页面，post是提交动作
@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginFrom()
    if request.method == 'POST':        
        if form.validate_on_submit():  #判断request是个带POST数据，且数据符合表单定义要求, 并且验证csrf通过
            _username = request.form.get('username')
            _password = request.form.get('password')
            LogUtils().info("登录信息：{},{}",_username,_password)
            if _username == "admin" and _password == "Aa111111":
                token = create_token(_username, _password)
                LogUtils().info(">>>>生成的token:{}", token)
                cache_add(DashboardConfig().get_config()['auth']['token_key'], token)
                return redirect(url_for('index'))
            else:
                LogUtils().info("用户名或者密码错误，返回错误信息")        
        else:
            LogUtils().info("登录失败，返回错误信息")
    return render_template('login.html',form=form)

# 登出操作
@app.route('/logout',methods=['GET','POST'])
def logout():
    #删除token
    cache_del(DashboardConfig().get_config()['auth']['token_key'])

    form=LoginFrom()
    return render_template('login.html',form=form)
######################  >>>>> login  start <<<<<  ###################


######################  >>>>> index  start <<<<<  ###################
# 首页
@app.route('/')
@app.route('/index')
#@login_required
def index():
    _jenkins_job_db = JenkinsJobDb()
    _job_list = _jenkins_job_db.get_job_list()

    _db_api = MachineDb()
    _machine_list = _db_api.get_machine_list()

    return render_template('index.html',title='盟秀Dashboard',job_list=_job_list,machine_list=_machine_list)
######################  >>>>> index  end <<<<<  ####################



######################  >>>>> machine  start <<<<<  #############
# module_route/module_machine.py 服务器操作
######################  >>>>> machine  end <<<<<  ###############

######################  >>>>> operation  start <<<<<  ###########
# module_route/module_common_opt.py 常用运维操作 
######################  >>>>> operation  end <<<<<  #############

######################  >>>>> task  start <<<<<  ################
# module_route/module_task.py 定时任务
######################  >>>>> machine  end <<<<<  ###############

######################  >>>>> jenkins  start <<<<<  #############
# module_route/module_jenkins.py Jenkins部署操作
######################  >>>>> jenkins  end <<<<<  ###############

######################  >>>>> cache  start <<<<<  ###############
# module_route/module_cache.py 缓存操作
######################  >>>>> cache  end <<<<<  #################

######################  >>>>> ansible  start <<<<<  #############
# module_route/module_ansible.py 使用ansible运维服务器操作
######################  >>>>> ansible  end <<<<<  ###############

# start server    
if __name__ == '__main__':
    # schedule 不能放这里，不然修改的时候实时编译会报线程错误，单独放出去弄了个接口
    #_task = CommonTask()
    #_task.start_task()

    # CSRF key,如果不需要这行可以去掉
    app.config['SECRET_KEY']='AASDFASDF'
    
    app.run(host='0.0.0.0',port=8088, debug=True)