from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField('姓名',max_length=20)
    class Meta():
        db_table = 'publish'


class Artic(models.Model):
    title = models.CharField('标题',max_length=50)
    publisher = models.ForeignKey(Publisher,null=True)
    class Meta():
        db_table = 'artic'