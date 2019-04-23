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
    url(r'05-filter/$',views.filter_show)
]