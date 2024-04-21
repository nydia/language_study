"""
七牛云文件上传
"""
from qiniu import Auth,put_file
import uuid
import base64
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
    
def qiniu_upload(base64_content_path):     
    #上传后保存的文件名
    unique_id = uuid.uuid4()
    hex_id = unique_id.hex
    keyList = ['test/',hex_id,'.png']
    key =  ''.join(keyList)
    
    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    
    #要上传文件的本地路径
    print("txt路径:" + base64_content_path)
    
    with open(base64_content_path,'rb') as f:
        image_base64 = f.read()
    # 看看image_base64类型是不是正确的“bytes”类型
    print(type(image_base64))
    # 解码图片
    img_head,img_context=image_base64.decode().split(",")  # 将base64_str以“,”分割为两部分
    imgdata = base64.b64decode(img_context)    # 解码时只要内容部分
    #将图片保存为文件
    localfile = ''.join([path_utils.get_base_dir(), str_utils.get_random_str(), '.png'])
    with open(localfile,'wb') as f:
        f.write(imgdata)
    
    # 临时文件
    # pathList = [img_path,'rocketmq2.png']
    # localfile = ''.join(pathList)
    
    ret, info = put_file(token, key, localfile, version='v2') 
    print(info)
    print("上传之后的key:" + ret['key'])
    return ''.join([qiniu_path_prefix, ret['key']])
    