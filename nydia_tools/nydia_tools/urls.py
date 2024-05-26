"""
URL configuration for nydia_tools project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # 默认模块的是ocrs
    path("", include("ocrs.urls")),
    # ocrs模块的url都加上了前缀 ocrs/
	path("ocrs/", include("ocrs.urls")),
    # files模块的url都加上了前缀 files/
    path("files/", include("files.urls")),
    # tools模块的url都加上了前缀 tools/
    path("tools/", include("tools.urls")),
    # gpt模块的url都加上了前缀 gpt/
    path("gpt/", include("gpt.urls")),
    # admin模块的url都加上了前缀 admin/
    path('admin/', admin.site.urls),
]
