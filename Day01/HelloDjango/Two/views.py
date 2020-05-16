from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Two.models import Student
import random


def index(request):
    return HttpResponse('Two index')


def add_student(request):

    student = Student()
    student.s_name = 'Jerry%d' % random.randrange(100)
    student.save()

    return HttpResponse('add student %s complete!'%student.s_name)


def get_student(request):

    students = Student.objects.all()

    for student in students:
        print(student.s_name)

    # return HttpResponse('Student List')

    content = {
        "hobby":"play games!",
        "students":students,
    }

    return render(request,'student_list.html',content)


def update_student(request):
    student = Student.objects.get(pk=2)

    student.s_name = 'Jack'

    student.save()

    return HttpResponse("Student Update Success!")


def delete_student(request):
    student = Student.objects.get(pk=3)

    student.delete()

