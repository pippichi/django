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
    url(r'^addpersons/',views.add_persons),
    url(r'^getpersons',views.get_persons),
    url(r'^addperson/',views.add_person),
    url(r'^getperson/',views.get_person),
]