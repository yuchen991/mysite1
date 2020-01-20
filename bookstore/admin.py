from django.contrib import admin

# Register your models here.
from bookstore.models import Book

class Book_Manager(admin.ModelAdmin):
    # admin 的字段
    list_display = ('id','title','pub','price','m_price')
    # 详情页连接
    list_display_links = ['title']
    list_filter = ['pub']
    search_fields = ['title']
    list_editable = ['price','m_price']

admin.site.register(Book,Book_Manager)