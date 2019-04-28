from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def product_details(request):
    goodid = request.GET['goodid']
    good = Goods.objects.get(id=goodid)
    goodimg = good.goodsimg_set.all()
    gooddetail = good.goodsdetail_set.all()
    goodscolor = good.goodscolor_set.all()
    promise = good.promise.all()
    return render(request,'product_details.html',locals())
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)