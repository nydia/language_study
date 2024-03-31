from django.urls import path

from . import views

urlpatterns = [
    path("file_upload_page", views.file_upload_page, name="file_upload_page"),
    path("file_upload", views.file_upload, name="file_upload"),
]