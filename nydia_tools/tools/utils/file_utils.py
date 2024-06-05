"""
读取文件
"""
import requests
import json


class FileUtil:
    def __init__(self) -> None:
        pass
    def down_file(self,url,file_path): # 下载远程文件
        r = requests.get(url, stream=True)
        with open(file_path, "wb") as f:
            for bl in r.iter_content(chunk_size=1024):
                if bl:
                    f.write(bl)
        return file_path
    def get_remote_file(self,url,local_file_path): # 获取远程文件内容 # tests.ToolsTest.test_get_remote_file
        file_path = self.down_file(url, local_file_path)
        with open(file_path, 'r') as f:
           file_content = f.read()
        return file_content
    def get_local_file(self, local_file_path): # 获取本地内容，转成json
        with open(local_file_path, 'r') as f:
           file_content = f.read()
        return file_content
    def get_remote_file_json(self,url,local_file_path): # 远程文件内容转为json #  tests.ToolsTest.test_get_remote_file_json
        file_content = self.get_remote_file(url,local_file_path)
        data = json.loads(file_content)
        return data
    def get_local_file_json(self, local_file_path): # 获取本地内容，转成json # tests.ToolsTest.test_get_local_file_json
        file_content = self.get_local_file(local_file_path)
        data = json.loads(file_content)
        return data
    
file_util = FileUtil()