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