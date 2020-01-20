from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('姓名',max_length=20)

class Book(models.Model):
    title = models.CharField('书名',max_length=20)
    author = models.ManyToManyField(Author)