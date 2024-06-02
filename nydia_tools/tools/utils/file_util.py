"""
读取文件
"""
import requests


class FileUtil:
    def __init__(self) -> None:
        pass
    def down_file(self,url,file_path):
        r = requests.get(url, stream=True)
        with open(file_path, "wb") as f:
            for bl in r.iter_content(chunk_size=1024):
                if bl:
                    f.write(bl)
        return file_path
    def get_url_file(self):
        #url = "https://gitee.com/techpj/quick_entry/blob/master/file.json"
        url = "http://qn.image.91ocr.asia/json/tools_json.txt"
        file_path = 'tools_json.txt'
        file_path = self.down_file(url, file_path)
        with open(file_path, 'r') as f:
            print(f.read())
        #_json = response.text
        print(file_path)
        pass
    def get_local_file(self):
        pass