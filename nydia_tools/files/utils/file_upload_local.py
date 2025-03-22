import os
"""
上传文件到gitee
"""

class FileUploadLocal:
    def __init__(self):
        pass
    def upload(self,file):
        file_path = os.path.join('files/file_path', file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return file_path
upload_local = FileUploadLocal()
