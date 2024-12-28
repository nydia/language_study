# _*_ coding:utf-8 _*_
import os
import subprocess

class AnsiblePlaybookOpt:
    def __init__(self) -> None:
        pass
    
    """获取playbook的文件根目录"""
    @staticmethod
    def get_playbook_basepath():
        # 项目名称
        p_name = 'dashboard-web-python'
        # 获取当前文件的绝对路径
        p_path = os.path.abspath(os.path.dirname(__file__)) 
        # 通过字符串截取方式获取
        root_path = p_path[:p_path.find(p_name) + len(p_name)]
        base_path = root_path + os.sep + "ansible_playbook" + os.sep
        return base_path
    
    """get server status"""
    @staticmethod
    def check_server_status(hostname):

        # 定义 ansible-playbook 命令
        #playbook_command = "ansible-playbook ansible_playbook/playbook-server-status.yml -i your_inventory_file"
        playbook_command = "ansible-playbook -e 'host_name="+hostname+"' " + AnsiblePlaybookOpt.get_playbook_basepath() + "playbook-server-status.yml" + " -i " + AnsiblePlaybookOpt.get_playbook_basepath() + "ansible_inventory"

        # 使用 subprocess 执行命令
        process = subprocess.Popen(playbook_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # 获取命令的输出结果
        stdout, stderr = process.communicate()

        result_stdout = stdout.decode('utf-8')
        result_stderr = stderr.decode('utf-8')
        return_code = process.returncode

        # 打印输出结果
        print("Stdout:\n" + result_stdout)
        print("Stderr:\n" + result_stderr)
        # 检查命令的返回码
        print("Return Code:\n", return_code)

        return result_stdout