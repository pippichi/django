from django.db import models

# Create your models here.

class Grade(models.Model):
    g_name = models.CharField(max_length=16,unique=True,db_column='class_name')


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_grade = models.ForeignKey(Grade)