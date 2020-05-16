import random
from io import BytesIO
from time import sleep

from PIL import Image, ImageFont
from PIL.ImageDraw import Draw, ImageDraw
from django.core.cache import caches
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


# @cache_page(30)
from django.views.decorators.csrf import csrf_exempt

from App.models import Student
from DjangoCache import settings


def news(request):

    cache = caches["redis_backend"]

    result = cache.get('news')

    if result:
        return HttpResponse(result)

    news_list = []

    for i in range(10):
        news_list.append(i)

    sleep(5)

    data = {
        'news_list':news_list,
    }

    response = render(request,'news.html',context=data)

    cache.set('news',response.content,timeout=60)

    return response

@cache_page(60,cache='default')
def jokes(request):

    sleep(5)

    return HttpResponse('JokeList')


def home(request):
    return HttpResponse('home')


def get_phone(request):

    if random.randrange(100) > 95:
        return HttpResponse('get the lottery')

    return HttpResponse('waiting in the line')


def get_ticket(request):
    return HttpResponse('get ticket')


def search(request):
    return HttpResponse('search')


def calc(request):

    a = 0

    b = 12

    result = b / a

    return HttpResponse(result)


@csrf_exempt
def login(request):

    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        return HttpResponse("post@")

def add_student(request):

    for i in range(100):

        student = Student()
        student.s_name = "xxsa%d"% i
        student.s_age = i%10 +15

        student.save()

    return HttpResponse("creation success!")

def get_students(request):

    page = int(request.GET.get('page',1))

    per_page = int(request.GET.get('per_page',10))


    students = Student.objects.all()[per_page*(page-1):per_page*page]

    return render(request,'students.html',context=locals())


def get_student_with_page(request):

    page = int(request.GET.get('page',1))

    per_page = int(request.GET.get('per_page',10))

    students = Student.objects.all()

    paginator = Paginator(students,per_page)

    page_object = paginator.page(page)

    data = {
        'page_object':page_object,
        'page_range':paginator.page_range,
        'tail_page':paginator.num_pages - 2,
        'head_page':3,
    }

    return render(request,"students_with_page.html",context=data)


def get_code(request):

    mode = "RGB"

    size = (200,100)

    color_bg = (255,0,0)

    image1 = Image.new(mode=mode,size=size,color=color_bg)

    imagedraw = ImageDraw(image1,mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH,50)

    imagedraw.text(xy=(0, 0), text='rock',font=imagefont)

    fp = BytesIO()

    image1.save(fp,"png")

    return HttpResponse(fp.getvalue(),content_type="image/png")