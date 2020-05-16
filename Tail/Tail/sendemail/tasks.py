"""
 -*- coding: utf-8 -*-
@File    : tasks.py
@Time    : 5/3/20 10:36 AM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""
from time import sleep

from celery import shared_task
from django.core.mail import send_mail

from Tail.settings import EMAIL_FROM


@shared_task
def add(a, b):
    print("go")
    sleep(5)

    return a + b


@shared_task
def send_email(receive):
    subject = "you are a little genis"
    message = "really!"

    from_email = EMAIL_FROM

    recipient_list = (receive,)

    send_mail(subject, message, from_email, recipient_list)
