from django.shortcuts import render
from .utils import file_utils
from .utils import json_utils
from .utils.watermark_utils import watermark_util
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

# 工具首页
def tools_index(request):
    context = {}
    return render(request, "tools/tools_index.html", context, None, None, None)

def tools_index2(request):
    fileUtil = file_utils.FileUtil()
    context = json_utils.serialize(fileUtil.get_url_file())
    print("------------------")
    print(context)
    return render(request, "tools/tools_index2.html", context, None, None, None)

# 去除水印页面
def tools_watermark(request):
    return render(request, "tools/tools_watermark.html", '', None, None, None)

# 去除水印操作
def watermark(request):
    watermark_util.remove_watermark('C:/temp/1.jpg','C:/temp/2.jpg')
    scripts = Scripts.objects.all()[0:1]
    json_data = serializers.serialize('json', scripts)
    return HttpResponse(json_data, content_type="application/json")