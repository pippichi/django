import logging

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from sendemail.tasks import add, send_email

log = logging.getLogger('mydjango')

def index(request):

    result = add(5,6)

    return HttpResponse(result)


def async(request):

    result = add.delay(5,6)

    return HttpResponse(result)


def email(request):

    try:
        mail_address = request.GET.get('address')
        send_result = send_email.delay(mail_address)
        return HttpResponse(send_result)
    except Exception as e:
        log.error(e)
    finally:
        return HttpResponse("fail")