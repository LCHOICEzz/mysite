#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/1 10:03 AM
# @Author  : Uji Zou
# @Site    :
# @File    : develop.py
# @Software: PyCharm

from .base import *  #NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}