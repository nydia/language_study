from django.urls import path

from . import views

urlpatterns = [
    path("toolindex",views.tools_index, name="tools_index"),
    path("toolindex2",views.tools_index2, name="tools_index2"),
    path('temp_file', views.temp_file, name='temp_file'),
    path('temp_file_upload', views.temp_file_upload, name='temp_file_upload'),
]