from django.urls import path

from . import views
from .sub_views import tools_home as tools_home


urlpatterns = [
    path("toolindex",views.tools_index, name="tools_index"),
    path('temp_file', views.temp_file, name='temp_file'),
    path('temp_file_upload', views.temp_file_upload, name='temp_file_upload'),
    
    # vue
    path("toolindex2",views.tools_index2, name="tools_index2"),
    
     # bootstrap4
    path("toolindex3",views.tools_index3, name="tools_index3"),
    
    # react
    path("toolhome",tools_home.tools_home, name="tools_home"),
    
]