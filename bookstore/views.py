

from django.core.paginator import Paginator
from django.core.validators import validate_email
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from bookstore.models import Book


def index_view(request):
    if request.method == 'GET':
        all_books = Book.objects.all()
        # 初始化分页对象,分页对象+每页多少个
        pageinator = Paginator(all_books,6)
        # c_page 具体页码的page对象,第一页
        page_num = request.GET.get('page',1)
        c_page = pageinator.page(page_num)
        return render(request,'bookstore/index.html',locals())
    elif request.method  == 'POST':
        return  HttpResponse('Please use GET method')

def sendemail_view(request):
    if request.method == 'GET':
        return render(request,'bookstore/sendemail.html')
    elif request.method == 'POST':
        users = request.POST.get('users')
        check_users = request.strip()
        user_list = [email.strip() for email in check_users.split(',')]
        _ = [validate_email(email) for email in user_list]
















