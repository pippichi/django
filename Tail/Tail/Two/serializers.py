"""
 -*- coding: utf-8 -*-
@File    : serializers.py
@Time    : 4/28/20 10:33 PM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from rest_framework import serializers

from Two.models import UserModel, AddressModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ('url', 'id', 'u_name', 'u_password')


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    address_list = UserSerializer(many=True,read_only=True)

    class Meta:
        model = AddressModel
        fields = ('url', 'id', 'a_address','address_list')
