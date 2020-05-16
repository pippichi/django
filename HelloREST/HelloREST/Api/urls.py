"""
# _*_ coding:utf-8 _*_
Name:.py
Date:
Auther:qyf
Connect:emoqyf@sina.com
"""
from django.conf.urls import url

from Api import views

urlpatterns = [
    url(r'^books/$', views.books, name='books'),
    url(r'^books/(?P<bookid>\d+)/',views.book,name="book"),
]
