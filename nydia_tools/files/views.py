import base64
from django.shortcuts import render

import json
from django.core import serializers
from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse

from django.http import HttpResponse

from .utils import file_upload_base
from .utils import user_utils
from .utils import path_utils
from .utils import str_utils

# Create your views here.

# 上下文
url_prefix = "http://127.0.0.1/"
page_title = "file upload"
copyright = "Copyright © 2024-2024 tools"
context = {}
context['page_title'] = page_title
context['copyright'] = copyright
context['url_prefix'] = url_prefix
    
# 适用于html文件在  nydia_tools/templates/files/upload.html
def file_upload_page(request):    
    if bool(user_utils.check_user()) == False:
        return render(request, "files/login.html", context, None, None, None)
    return render(request, "files/upload.html", context, None, None, None)

def file_upload(request):
    if bool(user_utils.check_user()) == False:
        return render(request, "files/login.html", context, None, None, None)    
    
    fileName = request.POST.get('fileName')
    print("文件名称： " + fileName)
    filePath = request.POST.get('filePath')
    print("文件目录： " + filePath)
    imgContent = request.POST.get('imgContent')
    #print("文件base64 " + imgContent)
    
    #要上传文件存放的本地根目录
    sys_base_path = path_utils.get_img_dir()
    
    # 文件名称
    random_str = str_utils.get_random_str()
    # txt文件
    path_txt_list = [sys_base_path, random_str, ".txt"]
    path_txt = ''.join(path_txt_list) 
    file=open(path_txt,'wt')#写成文本格式
    file.write(imgContent)
    file.close()
    
    # 方式1： 根据txt文件里面的base64图片内容生成图片上传到七牛云
    #img_path = file_upload_base.upload_by_txt_path(path_txt, filePath) 
    
    # 方式2： 根据base64图片内容生成图片上传到七牛云
    img_path = file_upload_base.upload_by_base64_content(imgContent, filePath) 

    return JsonResponse({'status': 'success','img_path': img_path})

def user_login_page(request):
    return render(request, "files/login.html", context, None, None, None)

def user_login(request):
    uname = request.POST.get('uname')
    upass = request.POST.get('upass')
    result = user_utils.user_login(uname, upass)
    if bool(result) == True:
        return JsonResponse({'status': 'success'})
        #return render(request, "files/upload.html", context, None, None, None) 
    else:
        return JsonResponse({'status': 'false'})   
        
    