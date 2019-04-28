from django.shortcuts import render

# Create your views here.


def index(request):
    "主页"
    return render(request,'index.html')

def header_show(request):
    "图片加载"
    return render(request,'header.html')
