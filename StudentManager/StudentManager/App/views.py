import hashlib
import random
import time
import uuid

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import Student


def register(request):
    if request.method == 'GET':
        return render(request, 'student_register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            student = Student()
            student.s_name = username
            student.s_password = password
            student.save()
        except Exception:
            return redirect(reverse('second:register'))
        return HttpResponse('register succeeded!')


def login(request):
    if request.method == 'GET':
        return render(request, 'student_login.html')
    elif request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        students = Student.objects.filter(s_name=username).filter(s_password=password)

        if students.exists():
            student = students.first()
            ip = request.META.get('REMOTE_ADDR')
            token = generate_token(ip, username)
            student.s_token = token
            student.save()

            # response = HttpResponse('login in!')
            # response.set_cookie("token",token)


            data = {
                "status": 200,
                "msg": "login success",
                "token": token,
            }

            # return response
            return JsonResponse(data=data)

        data = {
            "status": 404,
            "msg": "verify failed"
        }
        # return redirect(reversed('second:login'))
        return JsonResponse(data=data)


def generate_token(ip, username):
    c_time = time.ctime()

    # r = str(random.random())
    
    # return uuid.uuid4()

    return hashlib.new("md5", (ip + c_time + username).encode("utf-8")).hexdigest()


def student_mine(request):
    # token = request.COOKIES.get('token')
    token = request.GET.get('token')

    try:
        student = Student.objects.get(s_token=token)
    except Exception as e:
        return redirect(reverse("second:login"))

    # return HttpResponse(student.s_name)

    data = {
        "status": 200,
        "msg": "ok!",
        "data": {
            "username": student.s_name,
        }
    }
    return JsonResponse(data=data)
