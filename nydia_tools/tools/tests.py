from django.test import TestCase
from tools.utils.file_utils import file_util
from tools.utils.watermark_utils import watermark_util
import tools.utils.crawler_util

# Create your tests here.

"""
测试方式： python manage.py test tools.tests.ToolsTest

测试的方法必须以 test_ 开头
"""

#url = "https://gitee.com/techpj/quick_entry/blob/master/file.json"
url = "http://qn.image.91ocr.asia/json/tools_json.txt"
local_file_path = 'tools_json.txt'

# 公共测试
# python manage.py test tools.tests.ToolsTest
class ToolsTest(TestCase):
    def test_get_remote_file(self):
        print(f'remote file content : {file_util.get_remote_file(url,local_file_path)}')

    def test_get_remote_file_json(self):
        print(f'remote file json : {file_util.get_remote_file_json(url,local_file_path)}')
        
    def test_get_local_file_json(self):
        print(f'local file json : {file_util.get_local_file_json(local_file_path)}')
        
    def test_remove_watermark(self):
        watermark_util.remove_watermark('C:/temp/test1.jpg','C:/temp/test2.jpg')

# 水印测试
# python manage.py test tools.tests.ToolsTest_watermark
class ToolsTest_watermark(TestCase):
    def test_remove_watermark(self):
        watermark_util.remove_watermark('C:/temp/test1.jpg','C:/temp/test2.jpg')

 # 爬虫
# python manage.py test tools.tests.ToolsTest_crawler_news
class ToolsTest_crawler_news(TestCase):
    # 获取新闻数据
    news_data = tools.utils.crawler_util.get_latest_news()
    
    if news_data:
        # 同时保存三种格式
        tools.utils.crawler_util.save_to_file(news_data, format='txt')
        #tools.utils.crawler_util.save_to_file(news_data, format='csv')
        #tools.utils.crawler_util.save_to_file(news_data, format='json')
        
        # 打印前3条结果预览
        print("\n最新新闻预览：")
        for idx, news in enumerate(news_data[:3], 1):
            print(f"{idx}. [{news['time']}] {news['title']}")
    else:
        print("没有获取到新闻数据")