from django.urls import path

from . import views

urlpatterns = [
    path("toolindex",views.tools_index, name="tools_index"),
    path("toolindex2",views.tools_index2, name="tools_index2"),
]