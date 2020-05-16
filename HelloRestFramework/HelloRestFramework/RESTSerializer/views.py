from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.defaulttags import csrf_token
from django.views import View
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from RESTSerializer.models import Person, Student
from RESTSerializer.serializers import PersonSerializer, StudentSerializer


class PersonView(View):

    def get(self, request):
        persons = Person.objects.all()

        person_serializer = PersonSerializer(persons,many=True)

        return JsonResponse(person_serializer.data,safe=False)

    def post(self, request):
        p_name = request.POST.get('p_name')
        p_age = request.POST.get('p_age')

        person = Person()

        person.p_name = p_name
        person.p_age = p_age

        person.save()

        person_serializer = PersonSerializer(person)

        return JsonResponse(person_serializer.data)


class StudentView(APIView):
    def post(self, request,format=None):
        # s_name = request.POST.get('s_name')
        # s_age = request.POST.get('s_age')
        #
        # student = Student()
        #
        # student.s_name = s_name
        # student.s_age = s_age
        #
        # student.save()
        #
        # student_serializer = StudentSerializer(student)
        #
        # return JsonResponse(student_serializer.data)

        # data = JSONParser(request)
        # print(data)

        print(type(request))
        # print(type(request._request))
        print(request.GET)

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):

        student = Student.objects.all()
        serializer = StudentSerializer(student)
        return Response(serializer.data)


        # return JsonResponse({"msg":"ok"})
