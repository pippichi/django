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
    url(r'^register/', views.register, name="register"),
    url(r'^login/', views.login, name='login'),
    url(r'^studentmine/', views.student_mine, name='student_mine')
]
