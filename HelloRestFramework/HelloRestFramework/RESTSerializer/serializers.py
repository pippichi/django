"""
# _*_ coding:utf-8 _*_
Name:.py
Date:
Auther:qyf
Connect:emoqyf@sina.com
"""
from rest_framework import serializers

from RESTSerializer.models import Person, Student


class PersonSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    p_name = serializers.CharField(max_length=32)
    p_age = serializers.IntegerField(default=1)
    p_sex = serializers.BooleanField(default=False)

    def create(self, validated_data):
        Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.p_name = validated_data.get('p_name', instance.p_name)
        instance.p_age = validated_data.get('p_age', instance.p_age)
        instance.p_sex = validated_data.get('p_sex', instance.p_sex)
        instance.save()

        return instance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['s_age']
