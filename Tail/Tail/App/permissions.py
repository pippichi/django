"""
 -*- coding: utf-8 -*-
@File    : permissions.py
@Time    : 4/28/20 5:17 PM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from rest_framework.permissions import BasePermission

from App.models import UserModel


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            if isinstance(request.user, UserModel):
                return request.user.is_super
            return False
        return True