#!/usr/bin/eav python
# -*- coding:utf-8 -*-
#File
#Author:lin

#在jdango中能够给客户浏览器响应一段文本
from django.http import HttpResponse


def show_vie(request):
    """
    处理业务的视图处理函数
    :param request: 表示本次请求的请求对象封装请求所有消息
    :return:要响应给客户的内容
    """
    return HttpResponse("w1gcx")

def login(request):
    return HttpResponse("这是登录页面")

def register(request):
    return HttpResponse("这是注册页面")


def show_url(request,ye_int):
    return HttpResponse("我的值是： %s"%ye_int)


def show_int(request,n,y,r):
    return HttpResponse("日期： %s年 %s月 %s日"%(n,y,r))

def show_name(request,name,age):
    return HttpResponse("姓名：%s 年龄%s"%(name,age))