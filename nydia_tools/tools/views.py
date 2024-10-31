from django.shortcuts import render
from .utils import file_utils
from .utils import json_utils
from .utils.watermark_utils import watermark_util
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# 工具首页
def tools_index(request):
    context = {}
    return render(request, "tools/tools_index.html", context, None, None, None)

# 去除水印页面
def tools_watermark(request):
    return render(request, "tools/tools_watermark.html", '', None, None, None)

# 去除水印操作
def watermark(request):
    watermark_util.remove_watermark('C:/temp/1.jpg','C:/temp/2.jpg')
    scripts = Scripts.objects.all()[0:1]
    json_data = serializers.serialize('json', scripts)
    return HttpResponse(json_data, content_type="application/json")

# 上传文件 - 页面
def temp_file(request):
    context = {}
    return render(request, "tools/upload.html", context, None, None, None)

# 上传文件
@csrf_exempt
def temp_file_upload(request):
    if request.method == 'POST' and request.FILES.getlist('files'):
        password = fileName = request.POST.get('pass')
        print("pasword" + password)
        files = request.FILES.getlist('files')
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        for file in files:
            filename = fs.save(file.name, file)
        return HttpResponse('Files uploaded successfully.')
    return render(request, 'tools/upload.html')


# 工具首页- 结合vue
def tools_index2(request):
    # 从file获取url列表
    # fileUtil = file_utils.FileUtil()
    #context = {json_utils.serialize(fileUtil.get_url_file())}
    
    context = {}
    return render(request, "tools/vue/tools_index2.html", context, None, None, None)

# 工具首页- 结合boostrap4
def tools_index3(request):
    
    context = {}
    return render(request, "tools/boostrap4/tools_index.html", context, None, None, None)

