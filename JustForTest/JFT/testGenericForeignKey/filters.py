"""
 -*- coding: utf-8 -*-
@File    : filters.py
@Time    : 5/27/20 1:56 PM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
import django_filters

from testGenericForeignKey.models import User


class UserFilter(django_filters.FilterSet):
    # 按照id排序
    sort = django_filters.OrderingFilter(fields=('id'))

    # 股票代码、股票简称、拼音首字母的模糊查询
    u_name = django_filters.CharFilter(field_name='u_name', lookup_expr='icontains', label='name')

    class Meta:
        model = User
        fields = {
            'id': ['exact'],
        }
