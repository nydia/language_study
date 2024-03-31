from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ocr", views.easyocr_page, name="easyocr_page"),
    path("doocr", views.easyocr_page, name="easyocr_do"),
]