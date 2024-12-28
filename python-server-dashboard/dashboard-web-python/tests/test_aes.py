#-*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
from operation.operation import CommonOpt


class TestEncryptionDecryption(unittest.TestCase):
    def test_aes_decryption(self):
        #_result = CommonOpt.decrypt_sms_content("037a246df726fb7803a20b3ff0836901")
        #print(_result)
        CommonOpt.aes_decode("037a246df726fb7803a20b3ff0836901")

if __name__=='__main__':
    # 运行全部
    # unittest.main()

    # 运行部分
    suit = unittest.TestSuite()
    suit.addTest(TestEncryptionDecryption("test_aes_decryption"))
    runner = unittest.TextTestRunner()
    runner.run(suit) #运行测试用例 