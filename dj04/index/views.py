from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
import json
# Create your views here.




def index(request):
    return HttpResponse("aa")

def request_views(request):
    qq = ""
    qq += "<p>scheme %s</p>"%request.scheme
    qq += "<p>body %s</p>"%request.body
    qq += "<p>method %s</p>"%request.method
    qq += "<p>GET %s</p>"%request.GET
    qq += "<p>POST %s</p>"%request.POST
    qq += "<p>path %s</p>"%request.path
    qq += "<p>get_full_path %s</p>"%request.get_full_path()
    qq += "<p>get_host %s</p>"%request.get_host()
    qq += "<p>get_port %s</p>" % request.get_port()
    qq += "<p>COOKIES %s</p>"%request.COOKIES
    qq += "<p>session %s</p>"%request.session
    qq += "<p>META %s</p>"%request.META
    return HttpResponse(qq)

def get_show(request):
    if request.method == 'GET':
        if 'uname' in request.GET:
            if 'uage' in request.GET:
                qq = ""
                qq += request.GET['uname']
                qq += request.GET['uage']
                return HttpResponse(qq)
            return HttpResponse(request.GET['uname'])
        return HttpResponse('GET')
    elif request.method == 'POST':
        return HttpResponse('post')
    return HttpResponse()

def post_show(request):
    if request.method == 'GET':
        return render(request,'03-post.html')
    elif request.method == 'POST':
        if 'name' in request.POST:
            return HttpResponse("name: %s"%request.POST['name'])
        return HttpResponse("接收到但没有值")

def register_show(request):
    if request.method == 'GET':
        return render(request,'04-register.html')
    elif request.method == 'POST':
        qq = ""
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST['sex']
        hobby = request.POST.getlist('hobby')
        jg = request.POST['jg']

        qq = "%s "

        return
def form_show(request):
    if request.method == 'GET':
        form = RemaF()
        return render(request, '05-form.html', locals())
    elif request.method == 'POST':
        form = RemaF(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = Users(**form_data)
            user.save()
            return HttpResponse("ok")
        else:
            return HttpResponse("非法的")

def login_show(request):
    if request.method == 'GET':
        form = LoginF()
        return render(request, 'login.html', locals())
    elif request.method == 'POST':
        form = LoginF(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            form_name = form_data['uname']
            form_upwd = form_data['upwd']
            try:
                name = Users.objects.get(uname=form_name)
            except:
                return HttpResponse("没有该用户")
            if name:
                if form_upwd == name.upwd:
                    return HttpResponse("登入成功")
                else:
                    return HttpResponse("登入失败")
            else:
                return HttpResponse("没有该用户")
        else:
            return HttpResponse("非法的")

def logfor_show(request):
    if request.method == 'GET':
        form = LgW()
        return render(request, '07-logfor.html', locals())

def logincookie_show(request):
    if request.method == 'GET':
            return render(request,'08-logincookie.html')
    elif request.method == 'POST':
        name = request.POST.get('uname')
        pwd = request.POST['upwd']
        isA = request.POST.get('isA')
        try:
            ures = Users.objects.get(uname=name)
        except:
            return HttpResponse("用户名错误")
        if pwd == ures.upwd:
            print("!@@@")
            ps = 0
            if int(isA) == 1:
                ps = 60 * 60 * 24 * 30
            elif int(isA) == 2:
                ps = 60 * 60 * 24 * 30 * 6
            elif int(isA) == 3:
                ps = 60 * 60 * 24 * 365
            resp = HttpResponse("sss".encode())
            n = str(name).encode('gbk')
            p = str(pwd).encode('gbk')
            resp.set_cookie('uname'.encode('gbk'),n,ps)
            resp.set_cookie('upwd'.encode('gbk'),p,ps)
            print("ss##")
            return resp
        return HttpResponse("密码错误")

def setsess_show(request):
    request.session['uname'] = 'xiaos'
    request.session['upwd'] = '123'
    return HttpResponse("hao")

def getsess_show(request):
    uname = request.session.get('uname',"UnKnown")
    upwd = request.session.get('upwd', "UnKnown")
    return HttpResponse("%s %s"%(uname,upwd))


def server(request):
    name = request.GET['name']
    age = request.GET['age']
    qq = "姓名:%s  年龄:%s"%(name,age)
    return HttpResponse(qq)

def json_show(request):
    pr = {
        'name':'小虾',
        'age':20,
        'gender':'male',
        'email':'messa@12.com',
    }
    xl = json.dumps(pr)
    print(xl)
    return HttpResponse(xl)
def ajaxpsot(request):
    return render(request,'13-ajax-post.html')

def server13(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    pp = "%s %s"%(uname,upwd)
    print("ss",uname,upwd)
    return HttpResponse(pp)
