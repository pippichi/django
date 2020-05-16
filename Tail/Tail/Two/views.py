import uuid

from django.core.cache import caches
from django.shortcuts import render

# Create your views here.
from rest_framework import exceptions, status, viewsets
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response

from Two.auth import LoginAuthentication
from Two.constants import HTTP_ACTION_REGISTER, HTTP_ACTION_LOGIN
from Two.models import UserModel, AddressModel
from Two.permissions import Require_login_Permission
from Two.serializers import UserSerializer, AddressSerializer
from Two.throttles import UserThrottle


class UsersAPIView(CreateAPIView):
    serializer_class = UserSerializer

    queryset = UserModel.objects.all()

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
                    cache = caches['default']
                    token = uuid.uuid4()
                    cache.set(token, user.id)

                    data = {
                        "msg": "ok",
                        "status": status.HTTP_200_OK,
                        "token": token,
                    }
                    return Response(data=data)
                else:
                    raise exceptions.ValidationError
            except UserModel.DoesNotExist:
                raise exceptions.NotFound
        else:
            raise exceptions.ParseError


class UserAPIView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (LoginAuthentication,)
    permission_classes = (Require_login_Permission,)
    throttle_classes = (UserThrottle,)

    def retrieve(self, request, *args, **kwargs):
        # instance = self.get_object()
        # if instance.id == request.user.id:
        #     serializer = self.get_serializer(instance)
        #     return Response(serializer.data)
        # else:
        #     raise exceptions.AuthenticationFailed
        if kwargs.get("pk") != request.user.id:
            raise exceptions.AuthenticationFailed
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AddressAPIView(viewsets.ModelViewSet):
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = (LoginAuthentication,)
    permission_classes = (Require_login_Permission,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if kwargs.get('pk') == str(request.user.id):
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            raise exceptions.AuthenticationFailed

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = request.user

        a_id = serializer.data.get('id')

        try:
            address = AddressModel.objects.get(pk=a_id)

            address.a_user = user

            address.save()
        except AddressModel.DoesNotExist:
            raise exceptions.NotFound

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.queryset.filter(a_user=request.user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
