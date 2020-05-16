from django.db import models

# Create your models here.
class Book(models.Model):

    b_name = models.CharField(max_length=32)
    b_price = models.IntegerField(default=1)