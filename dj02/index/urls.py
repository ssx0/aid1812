#!/usr/bin/eav python
# -*- coding:utf-8 -*-
#File
#Author:lin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.show),
    url(r'^show/$',views.show),
    url(r'^01-temp/$',views.temp),
    url(r'^02-var1/$',views.var1),
]
urlpatterns += [
    url(r'^show-static/$',views.static_show)
]