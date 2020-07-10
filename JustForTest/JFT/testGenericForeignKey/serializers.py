"""
 -*- coding: utf-8 -*-
@File    : serializers.py
@Time    : 5/27/20 10:56 AM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from rest_framework import serializers

from testGenericForeignKey.models import User, Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    u_group = GroupSerializer()

    class Meta:
        model = User
        fields = ('id', 'u_name', 'u_group')
