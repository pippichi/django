"""
# _*_ coding:utf-8 _*_
Name:.py
Date:
Auther:qyf
Connect:emoqyf@sina.com
"""
from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index, name="index"),
    url(r'^uploadfile/', views.upload_file, name="upload_file"),
    url(r'^imagefield/', views.image_field, name="image_field"),
    url(r'^mine/',views.mine,name="mine"),
]
