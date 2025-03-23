import json
import requests

from . import file_constants

"""
上传文件到gitee
"""

class FileUploadGitee:
    def __init__(self):
        pass
    def upload(self,file):
        upload_url = file_constants.UPLOAD_GITEE_HOST
        response = requests.post(upload_url, files={'file': file})

        if response.status_code == 200:
            resp_json = json.loads(response.text)
            if resp_json['errcode'] == 200:
                return resp_json['result']['upload_result']['remote_url']
            else:
                return "file upload error"
        else:
            return "file upload error"
upload_gitee = FileUploadGitee()