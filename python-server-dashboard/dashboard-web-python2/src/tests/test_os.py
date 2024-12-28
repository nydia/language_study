#-*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest


class TestEncryptionDecryption(unittest.TestCase):
    def test_os_path(self):
        # 项目名称
        p_name = 'dashboard-web-python2'
        # 获取当前文件的绝对路径
        p_path = os.path.abspath(os.path.dirname(__file__)) 
        # 通过字符串截取方式获取
        path = p_path[:p_path.index(p_name) + len(p_name)]
        print(path + os.sep + "src" + os.sep + "ansible_playbook" + os.sep + "playbook-server-status.yml")
        pass
        

if __name__=='__main__':
    # 运行全部
    # unittest.main()

    # 运行部分
    suit = unittest.TestSuite()
    suit.addTest(TestEncryptionDecryption("test_os_path"))
    runner = unittest.TextTestRunner()
    runner.run(suit) #运行测试用例 