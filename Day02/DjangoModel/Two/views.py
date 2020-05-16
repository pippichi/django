import random

from django.db.models import Max, Avg, F, Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from Two.models import User, Order, Grade, Student, Customer, Company, Animal


def get_user(request):

    username = 'nessie1'
    password = '41'

    users = User.objects.filter(u_name=username)

    if users.exists():
        user = users.first()

        if user.u_password == password:
            print('login in succeed!')
        else:
            print('wrong password!')
    else:
        print('user not exists!')

    return HttpResponse('processing...')

def add_users(request):

    for i in range(20):
        user = User.objects.create(u_name='nessie%d'%i,u_password=str(random.randrange(10))+"%d"%i)
        print(user.u_name)

    return HttpResponse('create complete!')


def get_users(request):

    users = User.objects.all()[1:4]
    # users = User.objects.filter(u_name__contains='H')

    user_dict = {
        "hobby":"coding",
        "time":"one year",
    }

    code = """
        <h2>sleep</h2>
        <script type="text/javascript">
            alert("your webset is being invaded")
            var lis = document.getElementsByTagName('li')
            for(var i=0;i<lis.length;i++){
                let li = lis[i]
                li.innerHTML = "ameria is one part of chinese territory!"
            }
        </script>
    """

    context = {
        "users":users,
        "user_dict":user_dict,
        "count":5,
        "code":code,
    }

    return render(request,'UsersList.html',context=context)


def get_orders(request):

    o = Order.objects.create()
    orders = Order.objects.filter(pk=1)

    for i in orders:
        print(i.o_num)

    return HttpResponse('orders_list obtaining!')


def get_grades(request):

    grades = Grade.objects.filter(student__s_name='Jack')

    global grade

    if grades.count()==1:
        grade = grades.first()

    print(grade.o_name)

    return HttpResponse('obtained!')


def get_customer(request):

    results = Customer.objects.aggregate(Avg('c_cost'))

    print(results)

    return HttpResponse('intercept cost succeed!')


def get_company(request):

    # #boys fewer than girls
    # companys = Company.objects.filter(c_boy_num__lt=F('c_girl_num'))

    companys = Company.objects.filter(Q(c_boy_num__gt=1) | Q(c_girl_num__lt=5))

    for company in companys:
        print(company.c_name)

    return HttpResponse('company obtained!')


def get_animals(request):

    # #before define customized manager
    # animals = Animal.a_m.filter(is_delete=False)
    #after define customized manager
    animals = Animal.a_m.all()

    Animal.a_m.create_animal('bobby')

    for animal in animals:
        print(animal.a_name)

    return HttpResponse('animal obtained!')


def temp(request):
    return render(request,'home.html',context={"title":"home"})


def home(request):
    return render(request,'home_mine.html')


def hehe(request):
    return HttpResponse('??')


def hehehe(request):
    return HttpResponse('???')

def index(request):
    #essentially it returns HttpResponse with our templates and context data which is a render-to-string
    # return render(request,'index.html')

    temp = loader.get_template('index.html')

    context = temp.render()

    return HttpResponse(context)