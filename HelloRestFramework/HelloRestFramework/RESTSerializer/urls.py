"""
# _*_ coding:utf-8 _*_
Name:.py
Date:
Auther:qyf
Connect:emoqyf@sina.com
"""
from django.conf.urls import url

from RESTSerializer import views

urlpatterns = [
    url(r'^persons/',views.PersonView.as_view(),name='persons'),
    url(r'^students/',views.StudentView.as_view(),name='students'),
]