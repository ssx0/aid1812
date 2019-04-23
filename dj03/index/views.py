import datetime
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#导入模型
from .models import *



def parent(request):
    name = "小王"
    return render(request,'01_parent.html',locals())


def child(request):
    name = "小白"
    return render(request,'02-child.html',locals())

def create(request):
    # au1 = Author.objects.create(name='小王',
    #                       age='30',
    #                       email='xiaowang@122.com'
    #                       )
    # print(au1)
    # pp = "%s %s %s %s"%(au1.id,au1.name,au1.age,au1.email)

    # au = Author(name="小吴",age="15")
    # au.email = "xaionw@12.com"
    # au.save()
    # pp = "%s %s %s %s" % (au.id, au.name, au.age, au.email)

    dic={
        "name":"小菜",
        "age":45,
        "email":"xiaocau@21.com",
        "isActive":False
    }
    cc = Author(**dic)
    cc.save()
    pp = "%s %s %s %s" % (cc.id, cc.name, cc.age, cc.email)
    return HttpResponse(pp)

def pbk(request):
    dic = {
        "title":"电饭锅",
        "publicate_date":"2021-2-2",
    }
    obj = Book(**dic)
    obj.save()
    return HttpResponse("book保存成功")

def retrieve(request):
    # ret = Author.objects
    # print(ret)

    qq = ""
    # ret = Author.objects.all()
    # for i in ret:
    #     ti = "%s %s %s %s %s"%(i.id,i.name,i.age,i.email,i.isActive)
    #     qq += "<p>"+ti+"</p>"
    #     print(ti)

    # at = Author.objects.values()
    # for i in at:
    #     ti = "%s %s %s %s %s"%(i['id'],i['name'],i['age'],i['email'],i['isActive'])
    #     qq += "<p>" + ti + "</p>"

    at = Author.objects.values_list()
    for i in at:
        ti = "%s  %s  %s  %s  %s"%(i[0],i[1],i[2],i[3],i[4])
        qq += "<p>" + ti + "</p>"
    return HttpResponse(qq)

def filter_show(request):
    qq = ""
    # tt = Author.objects.filter(id=1,name='小王')
    # if tt:
    #     for aa in tt:
    #         print(aa.name,aa.email)

    tt = Author.objects.filter()
    return HttpResponse(pp)




