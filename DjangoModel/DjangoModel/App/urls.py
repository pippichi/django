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
    url(r'^addperson/', views.add_person, name="add_person"),
    url(r'^addidcard/', views.add_idcard, name="add_idcard"),
    url(r'^bindcard/',views.bind_card,name="bind_card"),
    url(r'^removeperson/',views.remove_person,name="remove_person"),
    url(r'^removeidcard/',views.remove_idcard,name="remove_idcard"),
    url(r'^getperson/',views.get_person,name="get_person"),
    url(r'^getidcard/',views.get_idcard,name="get_idcard"),

    url(r'^addcustomer/',views.add_customer,name="add_customer"),
    url(r'^addgood/',views.add_good,name="add_good"),
    url(r'^addtocart/',views.add_to_cart,name="add_to_cart"),
    url(r'^getgoodslist/(?P<customerid>\d+)',views.add_goods_list,name="add_goods_list"),
]
