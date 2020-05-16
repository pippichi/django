from django.contrib import admin

# Register your models here.
from Two.models import UserModel, AddressModel

admin.register(UserModel)
admin.register(AddressModel)