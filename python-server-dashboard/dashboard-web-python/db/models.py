# _*_ coding:utf-8 _*_
import json
from flask_wtf import FlaskForm   #导入继承父类
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,DataRequired

# 返回DTO
class ResponseDTO:
    def __init__(self,code,desc,data):
        self.code = code
        self.desc = desc
        self.data = data

# DB实时机器信息
class Machine:
    def __init__(self, id, ip, cpu_total, cpu_use, cpu_rate, mem_total, mem_use, mem_free, mem_available, env, status, remark):
        self.id = id
        self.ip = ip
        self.cpu_total = cpu_total
        self.cpu_use = cpu_use
        self.cpu_rate = cpu_rate
        self.mem_total = mem_total
        self.mem_use = mem_use
        self.mem_free = mem_free
        self.mem_available = mem_available
        self.env = env
        self.status = status        
        self.remark = remark

# 服务器实时信息
class MachineRealInfo:
    def __init__(self):
        pass
    def build(self,mem_info,mem_total,mem_used,mem_free,mem_available,cpu_total,cpu_use,cpu_usage):
        self.mem_info = mem_info
        self.mem_total = mem_total
        self.mem_free = mem_free
        self.mem_used = mem_used
        self.mem_available = mem_available
        self.cpu_total = cpu_total
        self.cpu_use = cpu_use
        self.cpu_usage = cpu_usage
        return self

# 服务器CPU实时信息
class MachineRealCpuInfo:
    def __init__(self):
        pass
    def build(self,total_cpu_time,cpu_idle,cpu_usage):
        # cpu总时间
        self.total_cpu_time = total_cpu_time
        # cpu使用时间
        self.cpu_idle = cpu_idle
        # cpu使用率
        self.cpu_usage = cpu_usage
        return self

# Jenkins Job
class JenkinsJob:
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        _obj_dict = {}
        if hasattr(self,"env_dev_status"):
            _obj_dict['env_dev_status'] = self.env_dev_status
        if hasattr(self,"env_sit_status"):
            _obj_dict['env_sit_status'] = self.env_sit_status
        if hasattr(self,"env_pit_status"):
            _obj_dict['env_pit_status'] = self.env_pit_status
        if hasattr(self,"id"):
            _obj_dict['id'] = self.id
        return json.dumps(_obj_dict)
    def build(self,id,job_name,deploy_host_dev,deploy_host_sit,deploy_tm,deploy_option,branch,env,pit_auto_apply,project_id,create_tm,status,type,image_name,env_dev_status,env_sit_status,env_pit_status,update_tm):
        self.id = id
        self.job_name = job_name
        self.deploy_host_sit = deploy_host_sit
        self.deploy_host_dev = deploy_host_dev
        self.deploy_tm = deploy_tm
        self.deploy_option = deploy_option
        self.branch = branch
        self.env = env
        self.pit_auto_apply = pit_auto_apply
        self.project_id = project_id
        self.create_tm = create_tm
        self.status = status
        self.type = type
        self.image_name = image_name
        self.env_dev_status = env_dev_status
        self.env_sit_status = env_sit_status
        self.env_pit_status = env_pit_status
        self.update_tm = update_tm

    def build_server_state(self,id,env_dev_status,env_sit_status,env_pit_status): # 构建应用服务状态
        self.id = id
        if env_dev_status is not None:
            self.env_dev_status = env_dev_status
        if env_sit_status is not None:
            self.env_sit_status = env_sit_status
        if env_pit_status is not None:
            self.env_pit_status = env_pit_status
        return self

# 项目的git信息
class ProjectGitInfo:
    def __init__(self,project_id,name,path_with_namespace,description):
        self.project_id = project_id
        self.name = name
        self.path_with_namespace = path_with_namespace
        self.description = description

# 登录form
class LoginFrom(FlaskForm):  #继承自FlaskForm类
    username = StringField('用户名',validators=[Length(min=2,max=12,message='用户名长度为2~12位'),DataRequired(message='用户名不能为空')])
    password = PasswordField('密码',validators=[Length(min=2,max=12,message='密码长度为2~12位'),DataRequired(message='密码不能为空')])
    submit = SubmitField('登录')