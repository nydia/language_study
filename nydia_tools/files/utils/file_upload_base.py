"""
文件上传
"""

from . import file_upload_qiniu
    
# 上传文件流程：前端传来base64图片内容 -> 后台获取base64内容写入本地txt文件 -> 解析txt的base64内容写成图片 -> 上传本地图片内容到七牛云
def upload_by_txt_path(base64_local_path):
    return file_upload_qiniu.qiniu_upload_by_txt_path(base64_local_path)

# 上传文件流程：前端传来base64图片内容 -> 后台获取base64内容解析成图片 -> 上传本地图片内容到七牛云
def upload_by_base64_content(base64_content):
    return file_upload_qiniu.qiniu_upload_by_base64_content(base64_content)