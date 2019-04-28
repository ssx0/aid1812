from django.db import models
from userinfo.models import *
# Create your models here.


ORDER_STATUS = (
    (0, "未付款"),
    (1, "等待发货"),
    (2, "配送中"),
    (3, "已完成"),
    (4, "支付失败"),
    (5, "已取消"),
    (6, "订单关闭"),
)

COMPANY_INFO = (
    (0, "圆通快递"),
    (1, "申通快递"),
    (2, "中通快递"),
    (3, "顺丰快递"),
    (4, "EMS"),
    (5, "宅急送"),
)

class Order(models.Model):
    orderNo = models.CharField("订单号", max_length=20, null=False, default="abc")
    ads = models.TextField('收货信息')
    tomoney = models.DecimalField('总价格', max_digits=8, decimal_places=2)
    trmoney = models.DecimalField('实付价格', max_digits=8, decimal_places=2)
    amount = models.IntegerField("数量", null=True, default=0)
    bank = models.CharField("支付方式加卡号",max_length=50, null=False, default="unpay")
    dealtime = models.DateTimeField("交易时间", auto_now_add=True)
    status = models.IntegerField("订单状态", choices=ORDER_STATUS, null=False, default=0)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.orderNo


class OrderGoods(models.Model):
    title = models.CharField("商品名称", max_length=1000, null=False, default="商品名称")
    price = models.DecimalField('商品价格', max_digits=8, decimal_places=2)
    desc = models.CharField('描述', max_length=1000, null=True)
    amount = models.IntegerField("数量", null=True, default=0)
    color = models.CharField('颜色', max_length=50)
    spec = models.CharField('规格', max_length=50)
    goodsimg = models.ImageField("产品图", upload_to="ordersgood", default="normal.png")
    trprice = models.DecimalField('商品实际', max_digits=8, decimal_places=2)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)

    def __str__(self):
        return self.order.orderNo+self.title

    def __setitem__(self, k, v):
        self.k = v


class Logistics(models.Model):
    delivery_time = models.DateTimeField()
    logistics_company = models.IntegerField("物流公司", choices=COMPANY_INFO, default=0)
    express_number = models.CharField("快递编号", max_length=200, null=True, blank=True)
    order = models.OneToOneField(Order,on_delete=models.CASCADE)

    def __str__(self):
        return self.express_number


class LogisticsInfo(models.Model):
    information = models.CharField("物流信息", max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
    logist = models.ForeignKey(Logistics,on_delete=models.CASCADE)

    def __str__(self):
        return self.information