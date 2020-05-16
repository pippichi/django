"""
 -*- coding: utf-8 -*-
@File    : celery.py
@Time    : 5/3/20 10:17 AM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Tail.settings')

app = Celery('Tail')

app.config_from_object('django.conf:settings',namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
