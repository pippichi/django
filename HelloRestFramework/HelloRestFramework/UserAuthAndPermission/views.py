from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView

from UserAuthAndPermission.models import UserModel
from UserAuthAndPermission.serializers import UserSerializer


class UsersAPIView(ListCreateAPIView):

    serializer_class = UserSerializer

    queryset = UserModel.objects.all()

class UserAPIView(ListCreateAPIView):

    serializer_class = UserSerializer

    queryset = UserModel.objects.all()