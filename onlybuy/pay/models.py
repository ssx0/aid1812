from django.db import models
from userinfo.models import UserInfo
# Create your models here.

BANK_LIST = (
    (0, "未绑定"),
    (1, "工商银行"),
    (2, "建设银行"),
    (3, "中信银行"),
    (4, "中国银行"),
    (5, "支付宝"),
)


class Bank(models.Model):
    bank = models.IntegerField("绑定银行", choices=BANK_LIST, default=0)
    bankid = models.CharField("银行卡号", max_length=13, null=False)
    status = models.BooleanField("是否冻结", default=False)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Banklist(models.Model):
    bank = models.CharField("银行", max_length=100)
    bankimg = models.ImageField("logo", upload_to="banklist", default="logo.png")

    def __str__(self):
        return self.bank










