"""
# _*_ coding:utf-8 _*_
Name:.py
Date:
Auther:qyf
Connect:emoqyf@sina.com
"""
from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'^getuser/',views.get_user),
    url(r'^addusers/',views.add_users),
    url(r'^getusers/',views.get_users),
    url(r'^getorders/',views.get_orders),
    url(r'^getgrades/',views.get_grades),
    url(r'^getcustomer/',views.get_customer),
    url(r'^getcompany/',views.get_company),
    url(r'^getanimals/',views.get_animals),
    url(r'^temp/',views.temp),
    url(r'^home/',views.home),
    url(r'^hehe',views.hehe),
    url(r'^hehehe',views.hehehe),
    url(r'^index/',views.index),
]