"""
# _*_ coding:utf-8 _*_
Name:.py
Date:
Auther:qyf
Connect:emoqyf@sina.com
"""
from rest_framework.routers import DefaultRouter

from REST.views import UserViewSet, GroupViewSet, BookViewSet

router = DefaultRouter()

router.register(r'users',UserViewSet)
router.register(r'groups',GroupViewSet)
router.register(r'books',BookViewSet)