import base64
from django.shortcuts import render

import json
from django.core import serializers
from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse

from django.http import HttpResponse

from . import file_upload_qiniu

# Create your views here.

# 适用于html文件在  nydia_tools/templates/files/upload.html
def file_upload_page(request):
    context = {}
    context['page_title'] = "file upload"
    context['copyright'] = "Copyright © 2024-2024 tools"
    
    context['url_prefix'] = "http://127.0.0.1/"
    
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