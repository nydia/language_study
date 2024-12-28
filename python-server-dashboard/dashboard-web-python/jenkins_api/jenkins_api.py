#-*- coding:utf-8 -*-
import jenkins
from config.config_api import DashboardConfig
from utils.log_utils import LogUtils

class JenkinsApi:
    jen = object()
    def __init__(self) -> None: # 无参构造方法
        self.config = DashboardConfig().get_config()
    def login(self):
        self.jen = jenkins.Jenkins(url=self.config['jenkins']['url'], username=self.config['jenkins']['username'], password=self.config['jenkins']['password'])
        #print(self.jen.get_whoami())
    def job_list(self):
        mx_job_list = self.jen.get_all_jobs()
        #print(mx_job_list.__dict__)
        return mx_job_list
    def job_info(self,job_name):
        self.mx_job_info = self.jen.get_job_info(name=job_name)
        print(self.mx_job_info)
    def job_build_env_vars(self,job_name,build_n):
        self.mx_job_build_env_vars = self.jen.get_build_env_vars(name=job_name,number=build_n)
        print(self.mx_job_build_env_vars)
    def job_build(self, job_name, deploy_option, deploy_env, branche, pit_flg):
        try:
            parameters={'deploy_option':deploy_option,'branch':'origin/' + branche,'deploy_env':deploy_env,'pit_auto_apply':pit_flg} 
            self.jen.build_job(job_name, parameters)
        except Exception as e:
            LogUtils().info(">>>>>>构建失败: {}", e)
        finally:
            LogUtils().info("over")
    def get_branch(self, job_name):
        last_build_number = self.jen.get_job_info(job_name)['lastCompletedBuild']['number']
        build_info = self.jen.get_build_stages(job_name, last_build_number)
        branchs = []
        branch_list = build_info.get_revision_branch()
        for rev in branch_list:
            branchs.append(rev.get('name'))
        #rev = build_info.get_revision_branch()[0].get('name')
        return branchs
    def build_log(self, job_name):
        #last_build_number = self.jen.get_job_info(job_name)['lastCompletedBuild']['number']
        last_build_number = self.jen.get_job_info(job_name)['lastBuild']['number']
        out_put = self.jen.get_build_console_output(job_name, last_build_number) 
        # 获取job的最后一次构建的信息
        last_build_info = self.jen.get_build_info(job_name, last_build_number)
        # 获取job的最后一次构建是否还在构建中
        last_build_building = last_build_info['building']
        return out_put,last_build_building