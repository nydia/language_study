"""
七牛云文件上传
"""
from qiniu import Auth,put_file
import uuid
from nydia_tools import settings

#需要填写你的 Access Key 和 Secret Key
access_key = '3gVPGVw7N0TD3Ua4cIRun5_ZuGUEJ7z6lVMLVVy9'
secret_key = '04FmYX4VuARlhXwkSdp0_yYsd-uT9LbkkHz5Ncss'
#要上传的空间
bucket_name = 'blogghost'
#构建鉴权对象
q = Auth(access_key, secret_key)
    
def qiniu_upload(): 
    #上传后保存的文件名
    unique_id = uuid.uuid4()
    hex_id = unique_id.hex
    keyList = ['test/',hex_id,'.png']
    key =  ''.join(keyList)
    
    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    
    #要上传文件的本地路径
    base_path = settings.BASE_DIR.__str__()
    pathList = [base_path, '/files/file_path/','rocketmq2.png']
    localfile = ''.join(pathList)
    ret, info = put_file(token, key, localfile, version='v2') 
    print(info)