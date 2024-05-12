from django.urls import path

from . import views

urlpatterns = [
    path("toolindex",views.tools_index, name="tools_index"),
]