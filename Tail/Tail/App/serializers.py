"""
 -*- coding: utf-8 -*-
@File    : serializers.py
@Time    : 4/28/20 1:46 PM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from rest_framework import serializers

from App.models import UserModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ('url','id','u_name','u_password','is_super')