from django.db import models

# Create your models here.


class Promise(models.Model):
    title = models.CharField("承诺", max_length=30, null=False, default="承诺")
    desc = models.CharField('承诺描述', max_length=200, default='承诺商品描述')

    def __str__(self):
        return self.title

    class Meta():
        db_table = 'sale_promise'


class GoodsType(models.Model):
    title = models.CharField("分类名称", max_length=30, null=False, default="分类名称")
    desc = models.CharField('描述', max_length=200, default='商品描述')
    isDelete = models.BooleanField("是否下架",default=False)

    def __str__(self):
        return self.title

    class Meta():
        db_table = 'goods_type'


class Goods(models.Model):
    title = models.CharField("商品名称", max_length=1000, null=False, default="商品名称")
    price = models.DecimalField('商品价格', max_digits=8, decimal_places=2)
    desc = models.CharField('描述', max_length=1000, null=True)
    promise = models.ManyToManyField(Promise)
    listimg = models.ImageField("列表页图", upload_to="list", default="normal.png")
    isDelete = models.BooleanField("是否下架", default=False)
    type = models.ForeignKey(GoodsType,on_delete=models.CASCADE)


    def get_promise(self):
        return self.promise.title

    def __str__(self):
        return self.title


class GoodsDetail(models.Model):
    specifice = models.CharField("规格", max_length=100, null=False, default="规格")
    stock = models.IntegerField("库存", null=False, default=0)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)

    def __str__(self):
        return self.specifice


class GoodsColor(models.Model):
    color = models.CharField("颜色", max_length=30, null=False, default="颜色")
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)

    def __str__(self):
        return self.color


class GoodsImg(models.Model):
    goodsimg = models.ImageField("产品图", upload_to="goods", default="normal.png")
    goodsimgbig = models.ImageField("产品大图", upload_to="goods", default="normal.png")
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)

    def __str__(self):
        return self.goods.title



class Banner(models.Model):
    bannerimg = models.ImageField("论波图", upload_to="static/img/banner", default="normal.png")
    type = models.ForeignKey(GoodsType,on_delete=models.CASCADE)

    def __str__(self):
        return self.type.title
