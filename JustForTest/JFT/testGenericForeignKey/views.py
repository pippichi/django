from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response

from testGenericForeignKey.filters import UserFilter
from testGenericForeignKey.models import User, TestModel, Likes
from testGenericForeignKey.serializers import UserSerializer, GroupSerializer


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    queryset = User.objects.all()

    filter_backends = (DjangoFilterBackend,)

    filter_class = UserFilter

    def retrieve(self, request, *args, **kwargs):
        u_name = request.data.get("u_name")
        print(u_name)

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # if request.method  == 'POST':
        #     if serializer.data.get("u_name") == u_name:
        #         return Response({'msg': 'ok'})
        # else:
        #     return Response(serializer.data)

        return Response(serializer.data)
    def list(self, request, *args, **kwargs):
        u_name = request.data.get("u_name")
        u_name2 = request.query_params.get("u_name")

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)


        serializer = self.get_serializer(queryset, many=True)


        if request.method == 'POST':
            if u_name == serializer.data[0].get("u_name"):
                return Response({"msg": "ok"})
            else:
                return Response({"msg": "bad"})
        else:
            return Response(serializer.data)


class GroupView(viewsets.ModelViewSet):
    serializer_class = GroupSerializer


class LikesView(viewsets.ModelViewSet):
    pass

def test_page(request):
    testmodel = TestModel.objects.filter(id=1).first()
    test_model_ct = ContentType.objects.get_for_model(TestModel)
    total_like = len(Likes.objects.filter(content_type=test_model_ct, object_id=testmodel.id))
