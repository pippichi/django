"""
 -*- coding: utf-8 -*-
@File    : serializers.py
@Time    : 4/25/20 9:40 AM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from rest_framework import serializers

from UserAuthAndPermission.models import UserModel


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserModel

        fields = ('url','id','u_name','is_super')