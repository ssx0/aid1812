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
    url(r'08-logincookie/$',views.logincookie_show),
    url(r'09-setsess/$',views.setsess_show),
    url(r'10-getsess/$',views.getsess_show),
    url(r'12-server/$',views.server),
    url(r'13-json/$',views.json_show),
    url(r'13-ajax-post/$',views.ajaxpsot),
    url(r'13-server/$',views.server13),
]