from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def show_index(request):
    return HttpResponse("这是music下index")