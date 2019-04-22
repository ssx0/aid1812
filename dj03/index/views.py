from django.shortcuts import render
# Create your views here.




def parent(request):
    name = "小王"
    return render(request,'01_parent.html',locals())


def child(request):
    name = "小白"
    return render(request,'02-child.html',locals())