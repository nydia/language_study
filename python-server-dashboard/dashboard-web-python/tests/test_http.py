#-*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
from utils.http import HttpUtils
import requests
import json
from bs4 import BeautifulSoup


class TestHttp(unittest.TestCase):
    def test_simple(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_http_get_html(self):
        _data = HttpUtils.get_html("https://www.baidu.com")
        print("返回数据:", _data)
    def test_http_post(self):
        params_data = dict()
        params_data['loginName'] = '18301866076'
        params_data['password'] = 'Aa111111'
        params_data['smsCode'] = ''
        params_data['businessType'] = 1

        _params = dict()
        _params['params_type'] = 'form'
        #with open('data.json', 'w') as f:
        #    json.dump(_params,f)
        _params['params_data'] = json.dumps(params_data)

        _data = HttpUtils.post("http://10.200.200.145/gold-user-api/user/login", _params)
        #_data = requests.get("https://www.baidu.com").content.decode()
        print("返回数据:", _data)
    def test_html_parse(self):
        _data = HttpUtils.get_html("https://item.taobao.com/item.htm?id=642894884939").decode('utf-8')
        print(_data)
        soup = BeautifulSoup(_data,"html.parser")
        _test_img1 = soup.find_all('<meta',id='viewport')
        print(_test_img1)
        pass    

if __name__=='__main__':
    # 运行全部
    # unittest.main()

    # 运行部分
    suit = unittest.TestSuite()
    #suit.addTest(TestHttp("test_simple")) #把这个类中需要执行的测试用例加进去，有多条再加即可
    #suit.addTest(TestHttp("test_http_get_html")) #从上到下先后顺序
    #suit.addTest(TestHttp("test_http_post"))
    suit.addTest(TestHttp("test_html_parse"))
    runner = unittest.TextTestRunner()
    runner.run(suit) #运行测试用例 