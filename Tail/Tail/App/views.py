import uuid

from django.core.cache import caches
from django.shortcuts import render

# Create your views here.
from rest_framework import status, exceptions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from App.auth import UserAuth
from App.constants import HTTP_ACTION_LOGIN, HTTP_ACTION_REGISTER
from App.models import UserModel
from App.permissions import IsSuperUser
from App.serializers import UserSerializer
from Tail.settings import SUPER_USERS


class UsersAPIView(ListCreateAPIView):

    serializer_class = UserSerializer

    queryset = UserModel.objects.all()

    authentication_classes = (UserAuth,)

    permission_classes = (IsSuperUser,)

    # def get(self, request, *args, **kwargs):
    #     if isinstance(request.user,UserModel):
    #         if request.user.is_super:
    #             return self.list(request, *args, **kwargs)
    #         else:
    #             raise exceptions.NotAuthenticated
    #     else:
    #         raise exceptions.NotAuthenticated

    def post(self, request, *args, **kwargs):
        action = request.query_params.get('action')
        if action == HTTP_ACTION_REGISTER:
            return self.create(request, *args, **kwargs)
        elif action == HTTP_ACTION_LOGIN:
            u_name = request.data.get('u_name')
            u_password = request.data.get('u_password')

            try:
                user = UserModel.objects.get(u_name=u_name)
                if user.u_password == u_password:
                    token = uuid.uuid4().hex

                    cache = caches['default']
                    cache.set(token,user.id)

                    data = {
                        "msg":"login success",
                        "status":status.HTTP_200_OK,
                        "token":token,
                    }
                    return Response(data=data)
                else:
                    raise exceptions.AuthenticationFailed
            except UserModel.DoesNotExist:
                raise exceptions.NotFound
        else:
            raise exceptions.ValidationError


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        u_name = data.get('u_name')
        if u_name in SUPER_USERS:
            print('super user')
            u_id = serializer.data.get('id')
            user = UserModel.objects.get(pk=u_id)

            user.is_super = True

            user.save()

            data.update({'is_super': True})
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


    # def perform_create(self, serializer):
    #     serializer.save()
    #     data = serializer.data
    #     u_name = data.get('u_name')
    #     if u_name in SUPER_USERS:
    #         print('super user')
    #         u_id = serializer.data.get('id')
    #         user = UserModel.objects.get(pk=u_id)
    #
    #         user.is_super = True
    #
    #         user.save()
    #
    #         data.update({'is_super': True})
    #
    #     headers = self.get_success_headers(serializer.data)
    #
    #     return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class UserAPIView(ListCreateAPIView):

    serializer_class = UserSerializer

    queryset = UserModel.objects.all()