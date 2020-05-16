"""
 -*- coding: utf-8 -*-
@File    : urls.py
@Time    : 4/25/20 10:49 AM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from django.conf.urls import url

from UserAuthAndPermission import views

urlpatterns = [
    url(r'^users/$',views.UsersAPIView.as_view()),
    url(r'^users/(?P<pk>\d+)/$', views.UserAPIView.as_view(), name='usermodel-detail'),
]