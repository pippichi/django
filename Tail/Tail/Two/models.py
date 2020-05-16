from django.db import models

# Create your models here.

class UserModel(models.Model):
    u_name = models.CharField(max_length=16,unique=True)
    u_password = models.CharField(max_length=256)

    def __str__(self):
        return self.u_name

class AddressModel(models.Model):
    a_address = models.CharField(max_length=128)
    a_user = models.ForeignKey(UserModel,related_name="address_list",null=True,blank=True)
