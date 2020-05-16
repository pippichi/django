import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from App.models import Person


def add_persons(request):
    for i in range(15):
        person = Person()
        flag = random.randrange(100)
        person.p_name = "Tom%d" % i
        person.p_age = flag
        person.p_sex = flag % 2
        person.save()

    return HttpResponse("batch downloading!")


def get_persons(request):

    # persons = Person.objects.filter(p_age__gt=18).exclude(p_sex=False)

    persons = Person.objects.order_by("-p_age")

    persons_list = loader.get_template("PersonsList.html")

    context = {
        "persons":persons,
    }
    #
    # print(type(persons))

    result = persons_list.render(context=context)

    #test function values
    persons_values = persons.values()

    for person_value in persons_values:
        print(person_value)

    return HttpResponse(result)


def add_person(request):

    # person = Person.objects.create(p_name='mm',p_age=13,p_sex=True)

    person = Person.create('Jack')

    person.save()

    return HttpResponse("sunck")


def get_person(request):

    # person = Person.objects.get(p_age=20)
    #
    # print(person)

    person = Person.objects.all().first()

    print(person.p_name)

    person_one = Person.objects.all().last()

    print(person_one.p_name)

    return HttpResponse("obtain success!")