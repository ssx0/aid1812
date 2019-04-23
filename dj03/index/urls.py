#!/usr/bin/eav python
# -*- coding:utf-8 -*-
#File
#Author:lin

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^01-parent/$',views.parent),
    url(r'^02-child/$',views.child),
]
urlpatterns +=[
    url(r'^03-create/$',views.create),
    url(r'^03-book/$',views.pbk),
    url(r'^04-retrieve/$',views.retrieve),
    url(r'05-filter/$',views.filter_show),
    url(r'05-fil/$',views.filtershow),
    url(r'05-exclude/$',views.filter_exclude),
    url(r'05-get/$',views.get_show),
    url(r'05-count/$',views.count_show),
    url(r'06-aggreagte/$',views.aggreagte_show),
    url(r'06-annot/$',views.annot_show),
    url(r'06-lx/$',views.lx_show),
    url(r'06-cs/$',views.cs_show),
    url(r'06-ser/(\d+)/$',views.ser),
    url(r'06-dele/(\d+)/$',views.dele),
    url(r'06-ffl/$',views.fl),
]