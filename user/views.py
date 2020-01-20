import hashlib

from django.core import mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.utils.deprecation import MiddlewareMixin
from django.utils.encoding import smart_str

from note.views import login_check
from user.models import User


def registe_view(request):
    if request.method == 'GET':

        return render(request, 'user/registe.html')
    elif request.method == 'POST':
            username = request.POST.get('username')
            password_1 = request.POST.get('password_1')
            password_2 = request.POST.get('password_2')
            useremail = request.POST.get('email')
            user = User.objects.filter(username = username)
        # 判断用户
            if user:
                return HttpResponse('the user is existed')
            if not password_1:
                return HttpResponse('password is not the same')
            if password_1 != password_2:
                return HttpResponse('password is not the same')
            if not useremail:
                return HttpResponse('Please enter email')
            m = hashlib.md5(b'666')
            m.update(password_1.encode())
            try:
                user=User.objects.create(username=username,password=m.hexdigest(),email=useremail)

            except Exception as E:
                print('rigister error')
                print(E)
                return HttpResponse('server is busy')
            message = '欢迎%s的使用'%user.username
            mail.send_mail(subject='注册成功',
                           message=message,
                           from_email='yuchen651935@126.com',
                           recipient_list=[useremail])
            resp = HttpResponse('registered ok')
            resp.set_cookie('username',smart_str(user.username),expires=3600*24)
            # resp.set_cookie('uid',smart_str(user.id),expires=3600*24)
            request.session['uid'] = user.id
            return resp


def login_view(request):
    if request.method == 'GET':
        # 先判断session是否存在
        if request.session.get('uid') and request.session.get('username'):
            return HttpResponseRedirect('/index/')
        # 在判断cookies是否存在
        username = request.COOKIES.get('username')
        uid = request.COOKIES.get('uid')
        if username and uid:
            # 存在cookies则重写session
            request.session['uid'] = uid
            request.session['username'] = username
            return HttpResponse('/index/')
        # 都没有返回登录页面
        return render(request,'user/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username :
            return HttpResponse('please gove me right message')

        old_user = User.objects.filter(username=username)
        if not old_user:
            return HttpResponse('Username or password is wrong')
        # 校验密码
        m = hashlib.md5(b'666')
        m.update(password.encode())
        user = old_user[0]
        if user.password != m.hexdigest():
            return HttpResponse('password is wrong')
        request.session['uid'] = user.id
        request.session['username'] = user.username
        resp = HttpResponse('登录成功')
        # 判断issave这个键是否在提交上的表单来确定是否勾选
        if 'issave' in request.POST.keys():
            resp.set_cookie('uid',user.id,expires=3600*24)
            resp.set_cookie('username',user.username,expires=3600*24)
        return resp

def logout_view(request):
    if 'uid' in request.session:
        del request.session['uid']
    if 'username' in request.session:
        del request.session['username']
    resp = HttpResponse('已退出')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    return resp




















