"""
 -*- coding: utf-8 -*-
@File    : throttles.py
@Time    : 5/2/20 5:18 PM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from rest_framework.throttling import SimpleRateThrottle

from Two.models import UserModel


class UserThrottle(SimpleRateThrottle):
    scope = 'user'

    def get_cache_key(self, request, view):
        if isinstance(request.user,UserModel):
            ident = request.user.pk
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

class AddrThrottle(SimpleRateThrottle):
    scope = 'addr'

    def get_cache_key(self, request, view):
        if isinstance(request.user,UserModel):
            ident = request.user.pk
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }