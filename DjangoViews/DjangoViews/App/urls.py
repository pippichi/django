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
    # url(r'^students/$',views.students),
    url(r'^students/(\d+)/', views.student),
    url(r'^grades/', views.grades),
    url(r'^gettime/(\d+)/(\d+)/(\d+)/', views.get_time, name='get_time'),
    url(r'^getdate/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', views.get_date, name='getdate'),

    url(r'^learn/', views.learn, name='learn'),
    url(r'^haverequest/', views.haverequest),
    url(r'^createstudent/', views.create_student),
    url(r'^docreatestudent/', views.do_create_student, name='do_create_student'),
    url(r'^getticket/', views.get_ticket),

    url(r'^getinfo/', views.get_info, name='get_info'),
    url(r'^setcookie/', views.set_cookie, name='set_cookie'),
    url(r'^getcookie/', views.get_cookie, name='get_cookie'),

    url(r'^login/', views.login, name='login'),
    url(r'^dologin/', views.do_login, name='do_login'),
    url(r'^mine/', views.mine, name='mine'),
]
