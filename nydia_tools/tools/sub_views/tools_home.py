from django.shortcuts import render

# Create your views here.


# 工具home
def tools_home(request):
    context = {}
    return render(request, "tools/react/tools_home.html", context, None, None, None)
