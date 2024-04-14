import base64
from django.shortcuts import render

import json
from django.core import serializers
from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse

from django.http import HttpResponse

from .utils import file_upload_qiniu
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
    imgContent = request.POST.get('imgContent')
    #print("文件base64 " + imgContent)
    
    #要上传文件的本地路径
    img_path = path_utils.get_img_dir()
    
    random_str = str_utils.get_random_str()
    path_txt = [img_path, random_str, ".txt"]
    file=open(''.join(path_txt),'wt')#写成文本格式
    file.write(imgContent)
    file.close()
    
    path2 = [img_path, random_str, ".jpg"]
    file = open(''.join(path2),'wb')
    file.write(bytes(imgContent, 'utf-8'))
    file.close()
    
    path3 = [img_path, random_str, ".png"]
    with open(''.join(path3),'wb') as f:
        f.write(bytes(imgContent, 'utf-8'))
        
    img_path = file_upload_qiniu.qiniu_upload(path_txt)    

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
        
    