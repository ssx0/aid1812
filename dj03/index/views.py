import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum,Avg,Count,F
from django.shortcuts import redirect
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

    tt = Book.objects.filter(title__contains='a')
    for i  in tt:
        rr = "%s %s %s"%(i.id,i.title,i.publicate_date)
        qq += "<p>" + rr + "</p>"
    return HttpResponse(qq)

def filtershow(request):
    age30 = Author.objects.filter(age__gte=30)
    qq = ""
    qq += "<p>大于30：</p>"
    for ag in age30:
        r = "%s %s %s"%(ag.name,ag.age,ag.email)
        qq += "<p>" + r + "</p>"

    qq += "<p>有带王的：</p>"
    wang = Author.objects.filter(name__contains="王")
    for i in wang:
        rr = "%s %s %s" % (i.name, i.age, i.email)
        qq += "<p>" + rr + "</p>"

    qq += "<p>包含ao：</p>"
    ao = Author.objects.filter(email__contains="ao")
    for y in ao:
        rrr = "%s %s %s" % (y.name, y.age, y.email)
        qq += "<p>" + rrr + "</p>"

    qq += "<p>1990~2000年之间：</p>"
    tu = Book.objects.filter(publicate_date__year__range=(1990,2000))
    for l in tu:
        tt = "%s %s"%(l.title,l.publicate_date)
        qq += "<p>" + tt + "</p>"

    qq += "<p>大于小菜年龄的人：</p>"
    #先查询到小菜年龄取值
    # xiaocai = Author.objects.filter(name="小菜").values('age')
    #把查询到小菜年龄 作为值筛选所有人
    # suo = Author.objects.filter(age__gte=xiaocai)

    #简化 二合一
    xiaocai = Author.objects.filter(age__gte=\
            Author.objects.filter(name="小菜").values('age'))
    for ll in xiaocai:
        ttt = "%s %s %s" % (ll.name, ll.age, ll.email)
        qq += "<p>" + ttt + "</p>"


    return  HttpResponse(qq)

def filter_exclude(request):
    qq = ""
    ex = Author.objects.exclude(id=1)
    for ll in ex:
        ttt = "%s %s %s %s" % (ll.id,ll.name, ll.age, ll.email)
        qq += "<p>" + ttt + "</p>"
    return HttpResponse(qq)


def get_show(request):
    ii = Author.objects.get(id=1)
    print(ii)
    qq = "%s %s %s %s" % (ii.id,ii.name, ii.age, ii.email)
    return HttpResponse(qq)

def count_show(request):
    ii = Author.objects.filter().count()
    print(ii)
    return HttpResponse(ii)

def aggreagte_show(request):
    qq = ""
    rr = Author.objects.aggregate(
        jh=Sum('age'),
        he=Avg('age')
    )
    print(rr)
    qq += "<p>平均%.2f 总和%s </p>"%(rr['he'],rr['jh'])

    ss = Author.objects.filter(age__gte=30).aggregate(
        tj=Count('*'),
        pj=Avg('age')
    )
    qq += "<p>平均%.2f 人数%s </p>" % (ss['pj'], ss['tj'])

    return HttpResponse(qq)

def annot_show(request):
    qq = ""
    re = Author.objects.values('isActive').annotate(
        ct = Count('*'),
    )
    for i in re:
        qq += "<p>组：%s 人数%d" %(i['isActive'],i['ct'])
    print(re)
    return HttpResponse(qq)

def lx_show(request):
    qq = ""
    re = Book.objects.values('publicate_date').annotate(
        ct = Count('*'),
    )
    for i in re:
        qq += "<p>组：%s 数量%d" %(i['publicate_date'],i['ct'])
    return HttpResponse(qq)

def cs_show(request):
    re = Author.objects.filter(isActive=True)
    return render(request,'10-cs.html',locals())

def ser(request,id):
    re = Author.objects.get(id=id)
    return render(request,'10-ser.html',locals())

def dele(request,id):
    try:
        re = Author.objects.get(id=id)
        re.isActive = False
        re.save()
    except Exception as e:
        print(e)
    return redirect('/06-cs')

def fl(request):
    Author.objects.all().update(age=F('age')-10)
    return HttpResponse("ok")


