#!/usr/bin/eav python
# -*- coding:utf-8 -*-
#File
#Author:lin
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'01-request/$',views.request_views),
    url(r'02-get/$',views.get_show),
    url(r'03-post/$',views.post_show),
    url(r'04-register/$',views.register_show),
    url(r'05-form/$',views.form_show),
    url(r'06-login/$',views.login_show),
    url(r'07-logfor/$',views.logfor_show),
]