"""
 -*- coding: utf-8 -*-
@File    : tasks.py
@Time    : 5/2/20 8:27 PM
@Author   : qyf
Connect  : emoqyf@sina.com
@Software: Linux python3.6.8 Django2.0
"""

# #纯python情况下的celery
#
# from time import sleep
#
# from celery import Celery
#
# app = Celery("tasks",broker='redis://localhost:6379/1')
# app.conf.result_backend = 'redis://localhost:6379/0'
#
# @app.task
# def add(a,b):
#
#     sleep(4)
#
#     return a + b
#
# if __name__ == "__main__":
#     print(add.delay(4,3))
#     print(add.delay(4,3))
#     print(add.delay(4,3))
#     print(add.delay(4,3))
#     print(add.delay(4,3))
#     print(add.delay(4,3))
