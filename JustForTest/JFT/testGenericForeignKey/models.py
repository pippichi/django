from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Group(models.Model):
    g_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.g_name


class User(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_group = models.ForeignKey(to=Group, on_delete=models.CASCADE, blank=True, null=True, related_name="g")

    def __str__(self):
        return self.u_name

class TestModel(models.Model):
    title = models.CharField("测试模型", max_length=30)

class Likes(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
