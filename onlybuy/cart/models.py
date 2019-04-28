from django.db import models
from userinfo.models import UserInfo
from memberapp.models import *
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    color = models.CharField('颜色', max_length=50)
    spec = models.CharField('规格', max_length=50)
    price = models.DecimalField('价格', decimal_places=2, max_digits=8)
    amount = models.IntegerField("数量", null=True, default=0)

    def __str__(self):
        return self.user.username


class Favorite(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    color = models.CharField('颜色', max_length=50)
    spec = models.CharField('规格', max_length=50)

    def __str__(self):
        return self.user.username


class Buynow(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    color = models.CharField('颜色', max_length=50)
    spec = models.CharField('规格', max_length=50)
    amount = models.IntegerField("数量", null=True, default=0)

    def __str__(self):
        return self.user.username
