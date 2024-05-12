from django.shortcuts import render

# Create your views here.

context = {}

def tools_index(request):
    return render(request, "tools/tools_index.html", context, None, None, None)