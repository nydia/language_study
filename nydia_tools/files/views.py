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
from .utils.log_utils import log_util

# Create your views here.


url_prefix = "http://127.0.0.1/"
page_title = "file upload"
copyright = "Copyright © 2024-2024 tools"

# 适用于html文件在  nydia_tools/templates/files/upload.html
def file_upload_page(request):
    context = {}
    context['page_title'] = page_title
    context['copyright'] = copyright
    context['url_prefix'] = url_prefix
    
    return render(request, "files/upload.html", context, None, None, None)

def file_upload(request):
    fileName = request.POST.get('fileName')
    print("文件名称： " + fileName)
    imgContent = request.POST.get('imgContent')
    print("文件base64 " + imgContent)
    
    file=open('1.txt','wt')#写成文本格式
    file.write(imgContent)
    file.close()
    
    file = open('1.jpg','wb')
    file.write(bytes(imgContent, 'utf-8'))
    file.close()
    
    with open("2.png",'wb') as f:
        f.write(bytes(imgContent, 'utf-8'))
        
    file_upload_qiniu.qiniu_upload()    

    return JsonResponse({'status': 'success'})

def user_login_page(request):
    context = {}
    context['page_title'] = page_title
    context['copyright'] = copyright
    context['url_prefix'] = url_prefix
    
    return render(request, "files/login.html", context, None, None, None)

def user_login(request):
    uname = request.POST.get('uname')
    upass = request.POST.get('upass')
    user_utils.user_login(uname, upass)
    return JsonResponse({'status': 'success'})