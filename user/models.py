from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField('姓名',max_length=50,unique=True)
    password = models.CharField('密码',max_length=50)
    email = models.EmailField('邮箱',default='null')

    def __str__(self):
        return '用户'+ self.username