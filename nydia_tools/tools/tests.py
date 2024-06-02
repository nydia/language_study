from django.test import TestCase
from tools.utils.file_util import FileUtil

# Create your tests here.

# 测试方式： python manage.py test tools.tests.ToolsTest

class ToolsTest(TestCase):
    def test_file_util(self):
        fileUtil = FileUtil()
        fileUtil.get_url_file()
