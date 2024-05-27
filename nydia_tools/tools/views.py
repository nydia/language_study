from django.shortcuts import render
from .utils import file_read

# Create your views here.

context = {}

def tools_index(request):
    fileRead = file_read.FileRead()
    fileRead.get_url_file()
    return render(request, "tools/tools_index.html", context, None, None, None)