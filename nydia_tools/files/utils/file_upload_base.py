"""
文件上传
"""

from . import file_upload_qiniu
from .file_upload_gitee import upload_gitee
from .file_upload_local import upload_local
from .file_upload_alioss import upload_alioss
from . import file_constants
from .file_enum import StorageTypeEnum
    
# 上传文件流程：前端传来base64图片内容 -> 后台获取base64内容写入本地txt文件 -> 解析txt的base64内容写成图片 -> 上传本地图片内容到云服务（七牛云）
def upload_by_txt_path(base64_local_path, file_path):
    return file_upload_qiniu.qiniu_upload_by_txt_path(base64_local_path, file_path)

# 上传文件流程：前端传来base64图片内容 -> 后台获取base64内容解析成图片 -> 上传本地图片内容到云服务（七牛云）
def upload_by_base64_content(base64_content, file_path):
    return file_upload_qiniu.qiniu_upload_by_base64_content(base64_content, file_path)

# 上传文件流程：前端传来from表单 -> 后台解析流 -> 上传内容到云服务（gitee）
def upload_by_form(file):
    if file_constants.STORAGE == StorageTypeEnum.LOCAL:
        return upload_local.upload(file)
    elif file_constants.STORAGE == StorageTypeEnum.GITEE:
        # 上传文件流程：文件 -> nydia_tools项目 -> PlatformManager # pm-api -> gitee
        return upload_gitee.upload(file)
    elif file_constants.STORAGE == StorageTypeEnum.QINIU:
        pass
    elif file_constants.STORAGE == StorageTypeEnum.ALI_OSS:
        return upload_alioss.upload(file)
    elif file_constants.STORAGE == StorageTypeEnum.BAIDU_PAN:
        pass
    elif file_constants.STORAGE == StorageTypeEnum.ALI_PAN:
        pass

