from django.db import models


class user(models.Model):  # 用户模块
    objects = models.Manager()
    id = models.AutoField(primary_key=True)  # id
    name = models.CharField(max_length=100, null=True)  # 名字
    password = models.CharField(max_length=100, null=True)  # 密码
