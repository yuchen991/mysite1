from django.core import mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

# 装饰器检测用户
from note.models import Note

def login_check(fun):
    def wrap(request,*args,**kwargs):
        if not request.session.get('uid') or not request.session.get('username'):
            if not request.COOKIES.get('uid') or not request.COOKIES.get('username'):
                return render(request, 'user/login.html')
            else:
                uid=request.COOKIES.get('uid')
                username = request.COOKIES.get('username')
                request.session['uid'] = uid
                request.session['username'] = username
        # 将uid绑定给request
        # user = User.objects.get(id=uid)
        # request.my_user = user

        uid = request.session.get('uid')
        request.my_uid = uid
        return fun(request, *args, **kwargs)
    return wrap

def index_view(request):
    return HttpResponse('note index')

@login_check
def add_view(request):
    if request.method == 'GET':
        return render(request,'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if not title:
            return HttpResponse('Please give me title')
        if not content:
            return HttpResponse('Please give me content')
        Note.objects.create(title=title,content=content,user_id=request.my_uid)
        return HttpResponse('add OK')
    return HttpResponse('error')

@login_check
def list_view(request):
    if request.method == 'GET':
        uid = request.my_uid
        allnote = Note.objects.filter(user_id=uid)
        return render(request,'note/list_note.html',locals())
    else:
        return HttpResponse('Please give me GET')










