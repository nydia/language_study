#-*- coding:utf-8 -*-
import json
import unittest


class TestEncryptionDecryption(unittest.TestCase):
    def test_json(self):
        json_obj = {'name':'nicky'}
        json_str = json.dumps(json_obj)
        print(json_str)
        pass
        

if __name__=='__main__':
    # 运行全部
    # unittest.main()

    # 运行部分
    suit = unittest.TestSuite()
    suit.addTest(TestEncryptionDecryption("test_json"))
    runner = unittest.TextTestRunner()
    runner.run(suit) #运行测试用例 