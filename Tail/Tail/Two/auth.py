"""
 -*- coding: utf-8 -*-
@File    : auth.py
@Time    : 4/28/20 11:19 PM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from django.core.cache import caches
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from Two.models import UserModel


class LoginAuthentication(BaseAuthentication):
    def authenticate(self, request):
        cache = caches['default']
        token = request.query_params.get('token')
        user_id = cache.get(token)

        try:
            user = UserModel.objects.get(pk=user_id)
            return user, token
        except Exception:
            return
