from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.defaulttags import csrf_token
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from CBV.models import Book


class HelloCBV(View):
    msg = "hello"

    def get(self, request):
        return HttpResponse('%s ha' % self.msg)


class BoolsCBV(View):

    def get(self, request):
        book_list = Book.objects.all()

        book_list_json = []

        for i in book_list:
            book_list_json.append(i.to_dict())

        data = {
            "status": 200,
            "msg": "ok",
            "data": book_list_json
        }
        return JsonResponse(data=data)

    def post(self, request):
        b_name = request.POST.get('b_name')
        b_price = request.POST.get('b_price')

        book = Book()

        book.b_name = b_name
        book.b_price = b_price
        book.save()

        data = {
            "status": 201,
            "msg": "add success",
            "data": book.to_dict(),
        }

        return JsonResponse(data=data)


class HelloTemplateView(TemplateView):
    template_name = 'templateView.html'


class HelloListView(ListView):
    template_name = 'BookList.html'
    model = Book

class HelloDetailView(DetailView):

    # template_name = 'Book.html'

    model = Book