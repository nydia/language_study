import requests

"""
上传文件到gitee
"""

class FileUploadGitee:
    def __init__(self):
        pass
    def upload(self,file):
        upload_url = 'http://127.0.0.1:8081/upload'
        response = requests.post(upload_url, files={'file': file})
        if response.status_code == 200:
            return "filepath success"
        else:
            return "filepath error"
upload_gitee = FileUploadGitee()