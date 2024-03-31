from django.shortcuts import render

import json
from django.core import serializers
from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse


# Create your views here.

# 适用于html文件在  nydia_tools/templates/files/upload.html
def file_upload_page(request):
    context = {}
    context['page_title'] = "file upload"
    context['copyright'] = "Copyright © 2024-2024 tools"
    return render(request, "files/upload.html", context, None, None, None)

def file_upload(request):
    scripts = Scripts.objects.all()[0:1]
    json_data = serializers.serialize('json', scripts)
    return HttpResponse(json_data, content_type="application/json")