# _*_ coding:utf-8 _*_
import paramiko
import logging
import re
import time
from config.config_api import DashboardConfig
from config.constants import Constants
from db.models import MachineRealInfo,Machine,MachineRealCpuInfo
from db.machine_db import MachineDb
from utils.log_utils import LogUtils
from utils.str_utils import StrUtils

"""
获取Linux服务器的内存，CPU实时信息
"""

class MachineApi: 
    def __init__(self) -> None:
        self.config = DashboardConfig().get_config()

    def shell_execute(self, hostname, username, password, commd): # 执行shell脚本(复杂命令)
        _exec_result = ""
        try:
            LogUtils().info(">>>>>>执行shell脚本: [hostname={},username={},password={},command={}]", hostname,username,password,commd)

            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 建立 SSH 连接
            ssh_client.connect(hostname, username=username, password=password)

            # 执行命令获取内存信息: stdin为输入的命令 stdout为命令返回的结果 stderr为命令错误时返回的结果
            #stdin, stdout, stderr = ssh_client.exec_command("/opt/appl/spring-cloud/gold-soa-data-delete.sh dev 18301866076 Aa111111 20230605 CHANNEL_1001_MOBAOPAY")
            stdin, stdout, stderr = ssh_client.exec_command(commd)
            str_out_arr = []
            str_err_arr = []
            for x in stdout.readlines():
                str_out_arr.append(x.strip('\n'))
            for x in stderr.readlines():
                str_err_arr.append(x.strip('\n'))
            
            if str_err_arr is not None and len(str_err_arr) > 0:
                LogUtils().info(">>>>>>服务器返回的错误信息：{}", str_err_arr)
            if str_out_arr is not None and len(str_out_arr) > 0:
                LogUtils().info(">>>>>>服务器返回数据：{}", str_out_arr)

            _exec_result = str_out_arr # 返回信息数组

        except Exception as e:
            LogUtils().info(">>>>>>连接服务器错误，错误原因：{}", e)
        finally:
            # 关闭SSH连接
            ssh_client.close()
        return _exec_result

    def command_execute(self, hostname, username, password, commd): # 执行shell命令(简单命令)
        _exec_result = ""
        try:
            LogUtils().info(">>>>>>执行shell命令: [hostname={},username={},password={},command={}]", hostname,username,password,commd)

            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 建立 SSH 连接
            ssh_client.connect(hostname, username=username, password=password)

            # 执行命令获取内存信息: stdin为输入的命令 stdout为命令返回的结果 stderr为命令错误时返回的结果
            #stdin, stdout, stderr = ssh_client.exec_command("cat /proc/meminfo")
            stdin, stdout, stderr = ssh_client.exec_command(commd)
            str_out = stdout.read().decode('utf-8')
            str_err = stderr.read().decode('utf-8')

            if str_err != "":
                LogUtils().info(">>>>>>错误信息: {}", str_err)
            else:
                LogUtils().info(">>>>>>服务成功返回信息: {}", str_out)
                _exec_result = str_out

        except Exception as e:
            LogUtils().info(">>>>>>连接服务器错误，错误原因：{}", e)
        finally:
            # 关闭SSH连接
            ssh_client.close()
        return _exec_result

    def get_machine_info(self, machine_id): # 从数据库获取机器信息（并同步到机器的实时信息到数据库）
        _db_api = MachineDb()
        _machine_info = _db_api.get_machine_info(machine_id)
        _username = ""
        _password = ""

        if _machine_info:
            if _machine_info.env is None:
                return Machine()
            else:
                if Constants.ENV_DEV_SH == _machine_info.env:
                    _username = self.config['machine']['dev-sh']['user']
                    _password = self.config['machine']['dev-sh']['pass']
                elif Constants.ENV_DEV == _machine_info.env:
                    _username = self.config['machine']['dev']['user']
                    _password = self.config['machine']['dev']['pass']
                elif Constants.ENV_SIT == _machine_info.env:
                    _username = self.config['machine']['sit']['user']
                    _password = self.config['machine']['sit']['pass']
                elif Constants.ENV_UAT == _machine_info.env:
                    _username = self.config['machine']['uat']['user']
                    _password = self.config['machine']['uat']['pass']
                elif Constants.ENV_PIT == _machine_info.env:
                    _username = self.config['machine']['pit']['user']
                    _password = self.config['machine']['pit']['pass']

                # 获取服务器真实信息
                machine_real_info = self.machine_info_realtime(_machine_info, _username, _password)
                #print("machine_real_info>>>>>>", machine_real_info.__dict__)

                _machine_info.cpu_use = machine_real_info.cpu_use
                _machine_info.cpu_total = machine_real_info.cpu_total
                _machine_info.cpu_rate = machine_real_info.cpu_usage
                _machine_info.mem_total = machine_real_info.mem_total
                _machine_info.mem_use = machine_real_info.mem_used
                _machine_info.mem_free = machine_real_info.mem_free
                _machine_info.mem_available = machine_real_info.mem_available

                # 更新数据库信息
                _db_api.update_machine_info(_machine_info)

                return _machine_info
        else:
            return Machine()

    def machine_info_realtime(self, machine_info, username, password): # 获取机器实时信息
        machine_real_info = MachineRealInfo()
        try:
            # 执行命令获取内存信息
            hostname = machine_info.ip
            _command = "cat /proc/meminfo"
            memory_output = self.command_execute(hostname, username, password, _command)
            LogUtils().info(">>>>>>memory_output: ", memory_output)
            if StrUtils.is_blank(memory_output):
                return machine_real_info
            
            # 解析内存信息
            memory_total = re.search(r'MemTotal:\s+(\d+) kB', memory_output).group(1)
            memory_free = re.search(r'MemFree:\s+(\d+) kB', memory_output).group(1)
            memory_available = re.search(r'MemAvailable:\s+(\d+) kB', memory_output).group(1)

            machine_real_info.mem_info = memory_output
            machine_real_info.mem_total = memory_total
            machine_real_info.mem_free = memory_free
            machine_real_info.mem_available = memory_available
            machine_real_info.mem_used = float(memory_total) - float(memory_free)

            # 执行命令获取 CPU 信息
            #stdin, stdout, stderr = ssh_client.exec_command("cat /proc/cpuinfo")
            #cpu_info = stdout.read().decode('utf-8').strip()
            machine_cpu_info = self.get_machine_cpuinfo(hostname, username, password)
            if machine_cpu_info:
                machine_real_info.cpu_total = machine_cpu_info.total_cpu_time
                machine_real_info.cpu_use = machine_cpu_info.cpu_idle
                machine_real_info.cpu_usage = machine_cpu_info.cpu_usage
            
            # 测试信息
            #print(">>>>>>>>>>>>>Remote memory_output:", memory_output)
            #print(">>>>>>>>>>>>>Remote cpu_info:", cpu_info)
            #print(">>>>>>>>>>>>>Remote memory_info:", memory_info)
            #print(">>>>>>>>>>>>>Remote machine_info:", machine_real_info.__dict__)
            #print(">>>>>>>>>>>>>machine_real_info.mem_used:", machine_real_info.mem_used)
            
        except Exception as e:
            LogUtils().info("连接服务器错误，错误原因：{}", e)
        return machine_real_info

    def get_machine_cpuinfo(self, hostname, username, password): # 获取机器CPU实时信息
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        machine_cpu_info = MachineRealCpuInfo()
        try:
           
            # 建立 SSH 连接
            ssh_client.connect(hostname, username=username, password=password)

            # 执行命令获取CPU信息： 取两次的平均值
            stdin, stdout, stderr = ssh_client.exec_command('cat /proc/stat | grep "cpu "')
            str_out = stdout.read().decode('utf-8')
            str_err = stderr.read().decode('utf-8')

            cpu_idle1 = 0
            total_cpu_time1 = 0
            if str_err != "":
                LogUtils().info(">>>>>>错误信息: {}", str_err)
            else:
                cpu_time_list = re.findall('\d+', str_out)
                cpu_idle1 = cpu_time_list[3]
                total_cpu_time1 = 0
                for t in cpu_time_list:
                    total_cpu_time1 = total_cpu_time1 + int(t)

            time.sleep(1)
        
            cpu_idle2 = 0
            total_cpu_time2 = 0
            stdin, stdout, stderr = ssh_client.exec_command('cat /proc/stat | grep "cpu "')
            str_out = stdout.read().decode()
            str_err = stderr.read().decode()
            if str_err != "":
                LogUtils().info(">>>>>>错误信息: {}", str_err)
            else:
                cpu_time_list = re.findall('\d+', str_out)
                cpu_idle2 = cpu_time_list[3]
                total_cpu_time2 = 0
                for t in cpu_time_list:
                    total_cpu_time2 = total_cpu_time2 + int(t)
            cpu_usage = round(1 - (float(cpu_idle2) - float(cpu_idle1)) / (total_cpu_time2 - total_cpu_time1), 2)
            #print('>>>>>>当前CPU使用率为:' + str(cpu_usage),",总的是CPU时间:",str(total_cpu_time2),",已经使用的CPU时间:",str(cpu_idle2))

            machine_cpu_info.total_cpu_time = self.jiffies_to_minutes(total_cpu_time2)
            machine_cpu_info.cpu_idle = self.jiffies_to_minutes(float(cpu_idle2))
            machine_cpu_info.cpu_usage = cpu_usage

            #print("machine_cpu_info >>>>>>>>>>> ",machine_cpu_info.__dict__)

        except Exception as e:
            LogUtils().info("连接服务器错误，错误原因：{}", e)
        finally:
            # 关闭SSH连接
            ssh_client.close()
        return machine_cpu_info

    def jiffies_to_seconds(self, jiffies, clock_hz=100): #将 jiffies 转换为秒,系统的时钟频率设置为 100 Hz 
        seconds = jiffies / clock_hz
        return seconds
    def jiffies_to_minutes(self, jiffies, clock_hz = 100): # 将 jiffies 转换为分钟,系统的时钟频率设置为 100 Hz
        seconds = jiffies / clock_hz
        minutes = seconds / 60
        return minutes

    def sync_machine_info(self): # 同步机器的实时信息到数据库
        _machine_db = MachineDb()
        _machine_list = _machine_db.get_machine_list()
        for machine in _machine_list:
            self.get_machine_info(machine.id)

    '''
    获取docker server 的状态
    hostname 服务地址
    username 服务器用户名
    password 服务器密码
    image_name 镜像名称
    '''
    def get_machine_docker_server_state(self, hostname, username, password, image_name):
        server_state = ""
        try:          
            # docker ps -a
            # status (created|restarting|running|removing|paused|exited|dead)
            # status 容器状态有7种：created 已创建/restarting 重启中/running 运行中/removing 迁移中/paused 暂停/exited 停止/dead 死亡

            # sudo docker inspect --format '{{.Name}} {{.State.Running}}' mengxiu-demo
            # 返回: /mengxiu-demo true 最后一个值 true/false

            _command = "sudo docker inspect --format '{{.Name}} {{.State.Running}}' " + image_name
            str_out = self.command_execute(hostname, username, password, _command)
            if StrUtils.is_not_blank(str_out):
                _match=re.compile(r'\S+') #匹配非空字符串
                #print(_match.findall('/mengxiu-demo true'))
                _arr = _match.findall(str_out)
                if _arr is not None and len(_arr) >= 2:
                    return _arr[1]

        except Exception as e:
            LogUtils().info(">>>>>>获取服务器的发布状态错误，错误原因：{}", e)
        return server_state