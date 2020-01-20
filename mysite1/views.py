import csv
import os

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from bookstore.models import Book
from mysite1 import settings


def index(request):
    html = '首页'
    print(request.path_info)
    return HttpResponse(html)


def pagen_view(request, n):
    html = '这是第%s个页面' % (n)
    return HttpResponse(html)


def page1_view(request):
    html = '这是第1个页面'
    return HttpResponse(html)


def login_view(request):
    return HttpResponse('OK')


def index_view(request):
    return HttpResponse('欢迎')


def test_view(request):
    dic = {}
    dic['uname'] = 'yuchen'
    dic['Person'] = Person()

    return render(request, 'test.html', dic)


class Person():
    def say(self):
        return 'Hello everyone'


def test_if(request):
    val = 5
    dic = {'val': val}
    return render(request, 'test_if.html', dic)


def test_static(request):
    return render(request, 'test_static.html')


def set_cookies(request):
    resp = HttpResponse('set_cookies')
    resp.set_cookie('username', 'yuchen', expires=120)
    return resp


def test_middle(request):
    print('test middle')
    return HttpResponse('test middleware is ok')

def test(request):
    return HttpResponse('test')

def test_load(request):
    if request.method == 'GET':
        return render(request,'test_load.html')
    elif request.method == 'POST':
        #上传文件
        load_file = request.FILES.get('myfile')
        # 拼接文件路径
        filename = os.path.join(settings.MEDIA_ROOT,load_file.name)
        with open(filename,'wb') as f:
            data = load_file.file.read()
            f.write(data)
        return HttpResponse('update file: %s OK'%(load_file.name))

def make_csv(request):
    page = request.GET.get('page')
    allbooks = Book.objects.all()
    P = Paginator(allbooks,2)
    # c_page 当前的页对象
    c_page = P.page(page)
    resp = HttpResponse(content_type='text/csv')
    resp['Content-Disposition'] = "attachment;filename='my.csv'"
    # 初始化csv 写入resp
    writer = csv.writer(resp)
    writer.writerow(['id','title','public','price','m_price'])
    for b in c_page:
        writer.writerow([b.id,b.title,b.pub,b.price,b.m_price])
    return resp






