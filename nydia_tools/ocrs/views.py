
import json
from django.core import serializers
from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the ocrs index.")

# 适用于html文件在  nydia_tools/ocrs/templates/ocrs/ocr.html
def easyocr_bak(request):
    temp = loader.get_template('ocrs/ocr.html')
    return HttpResponse(temp.render({'msg': 'hello,我是服务器复杂方式传递的数据'}, request))

# 适用于html文件在  nydia_tools/templates/ocrs/ocr.html
def easyocr_page(request):
    context = {}
    context['page_title'] = "tools"
    context['copyright'] = "Copyright © 2024-2024 tools"
    return render(request, "ocrs/ocr.html", context, None, None, None)

def easyocr_do(request):
    scripts = Scripts.objects.all()[0:1]
    json_data = serializers.serialize('json', scripts)
    return HttpResponse(json_data, content_type="application/json")