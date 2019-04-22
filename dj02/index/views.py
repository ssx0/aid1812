from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.


def show(request):
    return HttpResponse("我是主页")

def temp(request):
    return render(request,'01-si.html')

def var1(request):
    class Ain(object):
        name = "xiaobai"
        def eat(self):
            return self.name+" 在睡觉！！ "

    an = Ain()
    dic = {
        'uname':'luzemaria',
        'age':30,
        'salary':50000,
        'hobby':['ss','bb','bbb'],
        'foods':("??","tie","kongqi"),
        'films':{'msn':'!!!','xmx':'??????'},
        'animal':an
    }
    return render(request,'02-var1.html',dic)

def static_show(request):
    return render(request,'03-static_show.html')