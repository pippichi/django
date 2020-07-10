"""
 -*- coding: utf-8 -*-
@File    : urls.py
@Time    : 5/27/20 10:40 AM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from django.conf.urls import url

from testGenericForeignKey.views import UserView, GroupView

urlpatterns = [
    url(r'^user/', UserView.as_view({
        'post': 'list',
        'get': 'list'
    })),
    url(r'^group/', GroupView.as_view({
        'post': 'create'
    }))
]