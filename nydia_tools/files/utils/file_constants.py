from files.utils.file_enum import UploadTypeEnum
from files.utils.file_enum import StorageTypeEnum

"""
文件模块 - 类定义
UPLOAD_GITEE_HOST = 'http://127.0.0.1:8081/upload' 本地开发使用
ULOAD_GITEE_HOST = 'http://127.0.0.1:81/upload' pm内部访问自己的地址(nginx禁止访问pm项目)
UPLOAD_GITEE_HOST = 'http://172.17.0.1:81/upload' docker容器内部访问pm项目使用地址(nginx禁止访问pm项目)
UPLOAD_GITEE_HOST = 'http://www.aith.top/api/upload' 使用外网地址访问(nginx可以访问pm项目)
"""

UPLOAD_TYPE = UploadTypeEnum.FORM
STORAGE = StorageTypeEnum.GITEE
UPLOAD_TOKEN = 'W$8vWkLq3!xT5sZ9nY2pC7mF4rA1gH6jD0oKtQyVbNuI'
#UPLOAD_GITEE_HOST = 'http://127.0.0.1:8081/upload'
UPLOAD_GITEE_HOST = 'http://127.0.0.1:81/upload'
#UPLOAD_GITEE_HOST = 'http://172.17.0.1:81/upload'
#UPLOAD_GITEE_HOST = 'http://www.aith.top/api/upload'