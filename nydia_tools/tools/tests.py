from django.test import TestCase
from tools.utils.file_util import FileUtil

# Create your tests here.

# 测试方式： python manage.py test tools.tests.ToolsTest

#url = "https://gitee.com/techpj/quick_entry/blob/master/file.json"
url = "http://qn.image.91ocr.asia/json/tools_json.txt"
local_file_path = 'tools_json.txt'

class ToolsTest(TestCase):
    def test_file_util(self):
        fileUtil = FileUtil()
        print(f'file content : {fileUtil.get_remote_file(url,local_file_path)}')

    def test_file_json(self):
        fileUtil = FileUtil()
        print(f'json : {fileUtil.get_remote_json(url,local_file_path)}')