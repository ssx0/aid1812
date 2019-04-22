from django.db import models

# Create your models here.


#创建一个实体类
#Publisher(表示出版社的信息)
#django中允许省略自增的声明django会自动声明

#1.name：出版社名称(字符串)
#2.address:出版社所在的地址（字符串）
#3.city:出版所在的城市（字符串）
#4.country:出版社所在的国家（字符串）
#5.website:网址（字符串）

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()

