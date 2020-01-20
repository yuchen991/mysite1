from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from user.models import User


class User_Manager(admin.ModelAdmin):
    # admin 的字段
    list_display = ('id','username','password','email')
    # 详情页连接
    search_fields = ['username']

admin.site.register(User,User_Manager)