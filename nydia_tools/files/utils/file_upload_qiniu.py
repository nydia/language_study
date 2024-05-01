"""
七牛云文件上传
"""
import os
import uuid
import base64
from qiniu import Auth,put_file
from nydia_tools import settings
from . import path_utils
from . import str_utils

#需要填写你的 Access Key 和 Secret Key
access_key = '3gVPGVw7N0TD3Ua4cIRun5_ZuGUEJ7z6lVMLVVy9'
secret_key = '04FmYX4VuARlhXwkSdp0_yYsd-uT9LbkkHz5Ncss'
#要上传的空间
bucket_name = 'blogghost'
#构建鉴权对象
q = Auth(access_key, secret_key)

qiniu_path_prefix = "http://qn.images.lhqmm.com/"
qiniu_dir_default = 'test/'
dir_spliter = os.path.sep
qiniu_dir = qiniu_dir_default

# 上传文件流程：前端传来base64图片内容 -> 后台获取base64内容写入本地txt文件 -> 解析txt的base64内容写成图片 -> 上传本地图片内容到七牛云
def qiniu_upload_by_txt_path(base64_local_path, file_path):
    #打印要上传文件的本地txt路径
    print("txt路径:" + base64_local_path)
    
    print("file_path路径:" + file_path)
    qiniu_dir = qiniu_upload_dir(file_path)  
      
    #获取到txt里面的base64内容
    with open(base64_local_path,'rb') as f:
        image_base64 = f.read()
    # 看看image_base64类型是不是正确的“bytes”类型
    print(type(image_base64))
    
    # 解码图片： 从浏览器过来的图片有前缀 data:image/png;base64, 所以要把这个前缀去掉，取 iVBORw0KGgoAAA 后面的内容
    img_head,img_context=image_base64.decode().split(",")  # 将base64_str以“,”分割为两部分
    imgdata = base64.b64decode(img_context)    # 解码时只要内容部分
    #图片保存在本地的路径
    localfile = ''.join([path_utils.get_img_dir(), str_utils.get_random_str(), '.png'])
    # 把base64内容写入本地
    with open(localfile,'wb') as f:
        f.write(imgdata)
    
    # 临时文件
    # pathList = [img_path,'rocketmq2.png']
    # localfile = ''.join(pathList)
    
    #上传到七牛云后保存的文件名
    unique_id = uuid.uuid4()
    hex_id = unique_id.hex
    keyList = [qiniu_dir,hex_id,'.png']
    key =  ''.join(keyList)
    
    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    
    ret, info = put_file(token, key, localfile, version='v2') 
    print(info)
    print("上传之后的key:" + ret['key'])
    return ''.join([qiniu_path_prefix, ret['key']])
    
# 上传文件流程：前端传来base64图片内容 -> 后台获取base64内容解析成图片 -> 上传本地图片内容到七牛云
def qiniu_upload_by_base64_content(base64_content, file_path):
    #base64文件
    #print("base64文件:" + base64_content)
    
    print("file_path路径:" + file_path)
    qiniu_dir = qiniu_upload_dir(file_path)
    
    # 看看image_base64类型是不是正确的“bytes”类型
    print(type(base64_content))
    # str to bytes
    img_base64_content = bytes(base64_content, encoding = "utf8")
    
    # 解码图片： 从浏览器过来的图片有前缀 data:image/png;base64, 所以要把这个前缀去掉，取 iVBORw0KGgoAAA 后面的内容
    img_head,img_context=img_base64_content.decode().split(",")  # 将base64_str以“,”分割为两部分
    imgdata = base64.b64decode(img_context)    # 解码时只要内容部分
    #图片保存在本地的路径
    localfile = ''.join([path_utils.get_img_dir(), str_utils.get_random_str(), '.png'])
    # 把base64内容写入本地
    with open(localfile,'wb') as f:
        f.write(imgdata)
    
    #上传到七牛云后保存的文件名
    unique_id = uuid.uuid4()
    hex_id = unique_id.hex
    keyList = [qiniu_dir,hex_id,'.png']
    key =  ''.join(keyList)
    
    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    
    ret, info = put_file(token, key, localfile, version='v2') 
    print(info)
    print("上传之后的key:" + ret['key'])
    return ''.join([qiniu_path_prefix, ret['key']])

# 获取 文件上传到服务器的 文件目录
def qiniu_upload_dir(file_path):
    if str_utils.str_is_not_blank(file_path):
        return str(file_path) + str(dir_spliter)
    else:
        return qiniu_dir_default