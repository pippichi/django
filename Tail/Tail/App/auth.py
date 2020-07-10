"""
 -*- coding: utf-8 -*-
@File    : auth.py
@Time    : 4/28/20 4:41 PM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from django.core.cache import caches
from rest_framework.authentication import BaseAuthentication

from App.models import UserModel


class UserAuth(BaseAuthentication):

    def authenticate(self, request):

        if request.method == 'GET':

            token = request.query_params.get('token')

            try:
                cache = caches['default']
                u_id = cache.get(token)

                user = UserModel.objects.get(pk=u_id)

                return user, token
            except:
                return
