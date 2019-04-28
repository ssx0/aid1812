#!/usr/bin/eav python
# -*- coding:utf-8 -*-
#File
#Author:lin

from django import forms
from . import models

# kj = (
#     ("1","好评"),
#     ("2","中评"),
#     ("3","差评"),
# )
# class RemaF(forms.Form):
#     "描述一个表示评论内容的表单类"
#     # 评论标题 　文本框
#     title = forms.CharField(label='标题',required=False)
#     #电子邮件　　邮件框
#     email = forms.EmailField(label='邮箱',
#                              error_messages={
#                                  'required':'请填写你的邮箱'
#                              })
#     #评论内容　　多行框
#     message = forms.CharField(
#         label='内容',
#         widget=forms.Textarea
#     )
#     #评论级别　　下拉菜单
#     level = forms.ChoiceField(
#         label='评价级别',
#         choices=kj,
#     )
#     #是否保存   复选框
#     issav = forms.BooleanField(label='保存')

class RemaF(forms.Form):
    uname = forms.CharField(label='姓名')
    upwd = forms.CharField(label='密码',widget=forms.PasswordInput)
    uage = forms.IntegerField(label='年龄')
    uemail = forms.EmailField(label='邮箱')

class LoginF(forms.ModelForm):
    class Meta:
        model = models.Users
        fields = ['uname','upwd']
        labels = {
            'uname':'用户名',
            'upwd':'密码',
        }
        widgets = {
            'uname':forms.TextInput(
                attrs={'placeholder':'请输入用户名',}
            ),
            'upwd':forms.PasswordInput(
                attrs={'placeholder':'请输入用户密码',}
            ),
        }

class LgW(forms.Form):
    uname = forms.CharField(
        label='用户名称',
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':"请输入用户名称"
            }
        )
    )
    upwd = forms.CharField(
        label='用户密码',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "请输入用户密码"
            }
        )
    )