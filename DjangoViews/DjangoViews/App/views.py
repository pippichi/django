import random

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import Student, Grade


def students(request):
    return HttpResponse('get student list!')


def student(request,grade_id):

    student_list = Student.objects.filter(s_grade_id=grade_id)

    return render(request,'grade_student_list.html',context=locals())


def grades(request):

    grade_list = Grade.objects.all()

    return render(request,'grade_list.html',locals())


def get_time(request,hour,minute,second):
    return HttpResponse("Time %s: %s: %s" % (hour,minute,second))


def get_date(request,day,month,year):
    return HttpResponse("Time %s: %s: %s" % (year,month,day))


def learn(request):
    return HttpResponse('continue studying!')


def haverequest(request):

    print(request.path)

    print(request.method)

    print(request.GET)

    hobby = request.GET.getlist('hobby')

    print(hobby)

    print(request.POST)

    return None


def create_student(request):
    return render(request,'form_table_instance.html')


def do_create_student(request):

    print(request.method)

    # print(request.META)
    # for key in request.META:
    #     print(key,request.META.get(key))
    print(request.META.get('REMOTE_ADDR'))

    username = request.POST.get('username')

    return HttpResponse(username)


def get_ticket(request):

    url = reverse('app:learn')

    if random.randrange(10) > 5:
        # return HttpResponseRedirect(url)
        return redirect(url)

    return HttpResponse("congratulations!")


def get_info(request):

    data = {
        'status':200,
        'msg':'ok',
    }

    return JsonResponse(data=data)


def set_cookie(request):

    response = HttpResponse()

    response.set_cookie("username","Rock")

    return response


def get_cookie(request):

    username = request.COOKIES.get('username')

    return HttpResponse(username)


def login(request):
    return render(request,'logini.html')


def do_login(request):

    uname = request.POST.get("uname")

    response = HttpResponseRedirect(reverse('app:mine'))

    # response.set_cookie('uname',uname,max_age=60)
    response.set_signed_cookie('uname',uname,"Rock")

    return response


def mine(request):

    # uname = request.COOKIES.get('uname')
    uname = request.get_signed_cookie("uname",salt="Rock")

    if uname:
        return HttpResponse(uname)

