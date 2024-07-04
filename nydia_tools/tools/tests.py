from django.test import TestCase
from tools.utils.file_utils import file_util
from tools.utils.watermark_utils import watermark_util

# Create your tests here.

"""
测试方式： python manage.py test tools.tests.ToolsTest

测试的方法必须以 test_ 开头
"""

#url = "https://gitee.com/techpj/quick_entry/blob/master/file.json"
url = "http://qn.image.91ocr.asia/json/tools_json.txt"
local_file_path = 'tools_json.txt'

class ToolsTest(TestCase):
    def test_get_remote_file(self):
        print(f'remote file content : {file_util.get_remote_file(url,local_file_path)}')

    def test_get_remote_file_json(self):
        print(f'remote file json : {file_util.get_remote_file_json(url,local_file_path)}')
        
    def test_get_local_file_json(self):
        print(f'local file json : {file_util.get_local_file_json(local_file_path)}')
        
    def test_remove_watermark(self):
        watermark_util.remove_watermark('C:/temp/1.jpg','C:/temp/2.jpg')