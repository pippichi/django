"""
 -*- coding: utf-8 -*-
@File    : permissions.py
@Time    : 4/28/20 11:26 PM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from rest_framework.permissions import BasePermission

from Two.models import UserModel


class Require_login_Permission(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user,UserModel)

