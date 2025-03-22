
from enum import Enum

"""
文件模块 - 枚举定义
"""

class UploadTypeEnum(Enum):
    # Base64字节
    BASE64 = 1
    # form
    FORM = 2

class StorageTypeEnum(Enum):
    # gitee （调用PlatManager平台接口）
    GITEE = 1
    # 七牛
    QINIU = 2
    # 百度网盘（调用PlatManager平台接口）
    BAIDU_PAN = 3
    # 阿里网盘
    ALI_PAN = 4
    # 阿里云OSS
    ALI_OSS = 5