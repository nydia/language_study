"""
读取文件
"""
import requests


class FileRead:
    def __init__(self) -> None:
        pass
    def get_url_file(self):
        #file_path = "https://gitee.com/techpj/quick_entry/blob/master/file.json"
        file_path = "http://qn.image.91ocr.asia/json/tools_json.txt"
        response = requests.get(file_path)
        _json = response.text
        print(_json)
        pass
    def get_local_file(self):
        pass