"""
# _*_ coding:utf-8 _*_
Name:.py
Date:
Auther:qyf
Connect:emoqyf@sina.com
"""
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from Api.models import Book

def index(request):

    data = {
        "status":200,
        "msg":"ok"
    }

    return JsonResponse(data)

@csrf_exempt
def books(request):
    if request.method=='GET':
        book_list = Book.objects.all()

        book_list_json = []

        for book in book_list:
            book_list_json.append(book.to_dict())

        data = {
            "status":200,
            "msg":"ok",
            "data":book_list_json
        }
        return JsonResponse(data=data)

    elif request.method=='POST':
        b_name = request.POST.get('b_name')
        b_price = request.POST.get('b_price')

        book = Book()
        book.b_price = b_price
        book.b_name = b_name
        book.save()

        data = {
            'status':201,
            'msg':'add success',
            'data':book.to_dict(),
        }

        return JsonResponse(data=data,status=201)

@csrf_exempt
def book(request,bookid):
    if request.method=='GET':
        book = Book.objects.get(pk=bookid)

        data = {
            "status":200,
            "msg":"ok",
            "data":book.to_dict()
        }

        return JsonResponse(data=data)
    elif request.method=='DELETE':
        book = Book.objects.get(pk=bookid)

        book.delete()

        data = {
            "status":204,
            "msg":"delete success",
            "data":{}
        }

        return JsonResponse(data=data,status=204)