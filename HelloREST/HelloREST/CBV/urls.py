"""
# _*_ coding:utf-8 _*_
Name:.py
Date:
Auther:qyf
Connect:emoqyf@sina.com
"""
from django.conf.urls import url

from CBV import views

urlpatterns = [
    url(r'^hello/',views.HelloCBV.as_view(),name='hello'),
    url(r'^books/',views.BoolsCBV.as_view(),name='books'),
    url(r'^templateview/',views.TemplateView.as_view(template_name='templateView.html'),name='template_view'),
    url(r'^listview/',views.HelloListView.as_view(),name='listview'),
    url(r'^single/(?P<pk>\d+)/',views.HelloDetailView.as_view(),name='single'),
]