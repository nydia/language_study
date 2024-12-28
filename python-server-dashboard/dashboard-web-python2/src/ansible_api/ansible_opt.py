#-*- coding:utf-8 -*-
import os

# # 核心类
# # 用于读取YAML和JSON格式的文件
# from ansible.parsing.dataloader import DataLoader
# # 用于存储各类变量信息
# from ansible.vars.manager import VariableManager
# # 用于导入资产文件
# from ansible.inventory.manager import InventoryManager
# # 操作单个主机信息
# from ansible.inventory.host import Host
# # 操作单个主机组信息
# from ansible.inventory.group import Group
# # 存储执行hosts的角色信息
# from ansible.playbook.play import Play
# # ansible底层用到的任务队列
# from ansible.executor.task_queue_manager import TaskQueueManager
# # 核心类执行playbook
# from ansible.executor.playbook_executor import PlaybookExecutor
# from ansible.playbook import Playbook

# class AnsibleOpt:
#     def __init__(self):
#         pass

#     """获取playbook的文件根目录"""
#     @staticmethod
#     def get_playbook_basepath():
#         # 项目名称
#         p_name = 'dashboard-web-python2'
#         # 获取当前文件的绝对路径
#         p_path = os.path.abspath(os.path.dirname(__file__)) 
#         # 通过字符串截取方式获取
#         root_path = p_path[:p_path.index(p_name) + len(p_name)]
#         base_path = root_path + os.sep + "src" + os.sep + "ansible_api" + os.sep + "ansible_playbook" + os.sep
#         return base_path
    
#     """get server status"""
#     @staticmethod
#     def check_server_status():

#         # 定义 Ansible 的配置文件路径
#         ansible_cfg = '/etc/ansible/ansible.cfg'

#         # 创建数据加载器、变量管理器和清单管理器
#         loader = DataLoader()
#         inventory = InventoryManager(loader=loader)
#         var_manager = VariableManager(loader=loader, inventory=inventory)

#         # 将 Ansible 的配置文件路径添加到配置选项中
#         if os.path.isfile(ansible_cfg):
#             loader.configure(inventory=inventory, vars=var_manager, ansible_cfg=ansible_cfg)

#         # 定义 playbook 文件路径
#         playbook_path = AnsibleOpt.get_playbook_basepath() + "playbook-server-status.yml"

#         # 创建 playbook 对象
#         pb = Playbook.load(playbook_path, variable_manager=var_manager, loader=loader)

#         # 执行 playbook
#         pbex = PlaybookExecutor(playbooks=pb, inventory=inventory, variable_manager=var_manager, loader=loader)

#         # 执行 playbook
#         pbex.run()

#         pass