"""
 -*- coding: utf-8 -*-
@File    : urls.py
@Time    : 4/28/20 8:57 PM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from django.conf.urls import url

from Two.views import UserAPIView, UsersAPIView, AddressAPIView

urlpatterns = [
    url(r'^users/$',UsersAPIView.as_view()),
    url(r'^users/(?P<pk>\d+)/$',UserAPIView.as_view(),name='usermodel-detail'),
    url(r'^address/$',AddressAPIView.as_view({
        'post':'create',
        'get':'list',
    })),
    url(r'^address/(?P<pk>\d+)/$',AddressAPIView.as_view({
        'get':'retrieve',
    }),name='addressmodel-detail'),
]