"""
 -*- coding: utf-8 -*-
@File    : urls.py
@Time    : 5/3/20 10:37 AM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from django.conf.urls import url

from sendemail import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^async/', views.async),
    url(r'^email/',views.email),
]
