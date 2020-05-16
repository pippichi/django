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
    url(r'^news/', views.news, name='news'),

    url(r'^jokes/', views.jokes, name="jokes"),

    url(r'^home/', views.home, name="home"),

    url(r'^getphone/', views.get_phone, name="get_phone"),

    url(r'^getticket/', views.get_ticket, name='get_ticket'),

    url(r'^search/', views.search, name="search"),

    url(r'^calc/', views.calc, name="calc"),

    url(r'^login/', views.login, name="login"),

    url(r'^addstudent/', views.add_student, name="add_student"),
    url(r'^getstudents/', views.get_students, name="get_students"),

    url(r'^getstudentwithpage/',views.get_student_with_page,name="get_student_with_page"),

    url(r'^getcode/',views.get_code,name="get_code"),
]
