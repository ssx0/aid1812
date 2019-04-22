#!/usr/bin/eav python
# -*- coding:utf-8 -*-
#File
#Author:lin

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.show_index)
]