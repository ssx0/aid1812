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
    name = models.CharField(max_length=30,verbose_name="出版商")
    address = models.CharField(max_length=100,verbose_name="地址")
    city = models.CharField(max_length=50,verbose_name="城市")
    country = models.CharField(max_length=50,verbose_name="国籍")
    website = models.URLField(verbose_name="网站")

    class Meta:
        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = '出版商信息'

    def __str__(self):
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=50,db_index=True,verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    email = models.EmailField(null=True,verbose_name="邮箱")
    isActive = models.BooleanField(default=True,verbose_name="状态")

    class Meta:
        #数据表名
        db_table = 'author'
        #单数
        verbose_name = '作者'
        #复数
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100,verbose_name="图书名称")
    publicate_date = models.DateField(verbose_name="出版日期")

    class Meta:
        db_table = "book"
        verbose_name = '著作'
        verbose_name_plural = "书籍信息"

    def __str__(self):
        return self.title



