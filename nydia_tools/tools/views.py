from django.shortcuts import render
from .utils import file_utils
from .utils import json_utils

# Create your views here.

def tools_index(request):
    context = {}
    return render(request, "tools/tools_index.html", context, None, None, None)

def tools_index2(request):
    fileUtil = file_utils.FileUtil()
    context = json_utils.serialize(fileUtil.get_url_file())
    print("------------------")
    print(context)
    return render(request, "tools/tools_index2.html", context, None, None, None)