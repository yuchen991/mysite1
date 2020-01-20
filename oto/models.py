from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('姓名',max_length=50)

class Wife(models.Model):
    name = models.CharField('姓名',max_length=50)
    author = models.OneToOneField(Author,null=True)