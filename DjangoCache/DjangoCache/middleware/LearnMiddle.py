"""
# _*_ coding:utf-8 _*_
Name:.py
Date:
Auther:qyf
Connect:emoqyf@sina.com
"""

from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class HelloMiddle(MiddlewareMixin):

    def process_request(self,request):
        print(request.META.get("REMOTE_ADDR"))

        ip = request.META.get("REMOTE_ADDR")

        print(request.path)

        # if request.path == '/app/getphone/':
        #     if ip == "192.168.253.1":
        #         return HttpResponse(ip)
        #
        # if ip.startswith("10.0"):
        #     return HttpResponse('over')
        #
        # if request.path=='/app/search/':
        #     cache = caches["redis_backend"]
        #
        #     result = cache.get(ip)
        #     if result:
        #         return HttpResponse('visit too frequent')
        #     cache.set(ip,ip,timeout=10)

        # black_list = cache.get('black',[])
        #
        # print(black_list)
        #
        # if ip in black_list:
        #     return HttpResponse('negative')
        #
        # requests = cache.get(ip,[])
        #
        # requests.insert(0, time.time())
        # cache.set(ip, requests, timeout=60)
        #
        # while requests and time.time() - requests[-1] > 60:
        #     requests.pop()
        #
        # print(len(requests))
        #
        # if len(requests) > 15:
        #     black_list.append(ip)
        #     cache.set('black',black_list,timeout=60*60*4)
        #
        # if len(requests) > 10:
        #     return HttpResponse('too frequent!')

    def process_exception(self,exception,request):
        print(request,exception)
        return redirect(reverse("second:home"))

