import os
"""
上传文件到阿里oss
"""

class FileUploadAliOss:
    def __init__(self):
        pass
    def upload(self,file):
        # 连接到阿里云 OSS
        #auth = oss2.Auth(settings.OSS_ACCESS_KEY_ID, settings.OSS_ACCESS_KEY_SECRET)
        #bucket = oss2.Bucket(auth, settings.OSS_ENDPOINT, settings.OSS_BUCKET_NAME)
        #result = bucket.put_object(file.name, file)
        #if result.status == 200:
        #    print(f"文件 {file.name} 上传到 OSS 成功")
        #else:   
        #    print(f"文件 {file.name} 上传到 OSS 失败，状态码: {result.status}")
        pass
upload_alioss = FileUploadAliOss()    
