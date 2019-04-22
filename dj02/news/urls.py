#!/usr/bin/eav python3
# -*- coding:utf-8 -*-
#File
#Author:lin


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^show/$',views.show_vi)
]