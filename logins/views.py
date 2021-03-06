# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.serializers import serialize

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from logins.models import User


def index(request):
    acount = User.objects.all()
    template = loader.get_template('web/index.html')
    context = {
        'user': acount,
    }

    return HttpResponse(template.render(context, request))
    # return render(request, 'web/index.html')

def login(request):
    if request.method == 'POST':
        phone=request.POST.get('phone')
        password=request.POST.get('pass')
        if phone =='' or password =='':
            return render(request, 'web/login.html', {'code':300, 'mes': "Bạn phải nhập đầy đủ thông tin"})
        else:
            try:
                user = User.objects.get(phone=phone)
            except User.DoesNotExist:
                user = None
            if user is None :
                return render(request, 'web/login.html', {'code':300, 'mes': 'Tài khoản không tồn tại'})
            else:
                if user.password==password:
                    return render(request, 'web/login.html', {'code':200, 'mes': "Thành công"})
                else:
                    return render(request, 'web/login.html',  {'code':300, 'mes': "Sai mật khẩu"})

    return render(request, 'web/login.html')

def register(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('pass')
        email = request.POST.get('email')
        name = request.POST.get('name')
        birthday = request.POST.get('birthday')
        if phone=='' or password=='' or birthday=='':
            return render(request,'web/register.html',{'message': "bạn phải điền đầy đủ thông tin"})
        else:

            account= User(phone=phone,password=password,access_token="",name=name,email=email,birthday=birthday, role=1)
            account.save()
        return HttpResponseRedirect('/login',)

    return render(request, 'web/register.html')
def permission(request,phone):
    template = loader.get_template('web/permission.html')
    context = {
        'user': phone,
    }

    return HttpResponse(template.render(context, request))

