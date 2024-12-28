#-*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest

from config.config_api import DashboardConfig
from utils.cache import cache_add,cache_get

class TestConfig(unittest.TestCase):
    def test_simple(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_config(self):

        # --- 1. ---
        _config = DashboardConfig().get_config()
        _nodes = _config['cache']['redis']['sentinel-nodes']
        for e in _nodes:
            print(tuple(e))

        # --- 2. ---
        print(DashboardConfig().get_redis_nodes())

        # --- 3. ---
        cache_add('test_cache_2', '测试')

        # --- 4. ---
        print(cache_get('test_cache_2'))

        pass
        
if __name__=='__main__':
    # 运行全部
    # unittest.main()

    # 运行部分
    suit = unittest.TestSuite()
    suit.addTest(TestConfig("test_config"))
    runner = unittest.TextTestRunner()
    runner.run(suit) #运行测试用例 