# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-23 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20190423_1209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '著作', 'verbose_name_plural': '书籍信息'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': '出版社', 'verbose_name_plural': '出版商信息'},
        ),
        migrations.AlterField(
            model_name='book',
            name='publicate_date',
            field=models.DateField(verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='图书名称'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.CharField(max_length=100, validators=['地', '址']),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='city',
            field=models.CharField(max_length=50, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(max_length=50, verbose_name='国籍'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=30, validators=['出', '版', '商']),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(validators=['网', '站']),
        ),
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
        migrations.AlterModelTable(
            name='publisher',
            table='publisher',
        ),
    ]
