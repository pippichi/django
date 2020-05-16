from django.db import models

# Create your models here.

class UserModel(models.Model):
    u_name = models.CharField(max_length=16)

    # "upload_to" points to a relative path "MEDIA_ROOT" which is a media root path.
    u_icon = models.ImageField(upload_to='%Y/%m/%d/icons')