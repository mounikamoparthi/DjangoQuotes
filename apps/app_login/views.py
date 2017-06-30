# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse

def index(request):
    #User.objects.all().delete()
    #context = {
     #   'users' :  User.objects.all()
    #}
    return render(request,'app_login/index.html') #context

def registration(request):
    result = User.objects.register(request.POST)
    print result['status']
    if not result['status']:
        for error in result['errors']:
            print "In ERRORS"
            messages.error(request,error)
        return redirect(reverse('auth:index'))
    else:
    
        messages.success(request,"Successful")
        request.session['name'] = result['user'].name
        request.session['emailid'] = result['user'].emailid
        request.session['username'] = result['user'].username
        request.session['userid'] = result['user'].id
        
        return redirect(reverse('quotes:index')) #change here

def loginuser(request):
    result = User.objects.loginval(request.POST)
    if not result['status']:
        for error in result['errors']:
            messages.error(request,error)
        return redirect(reverse('auth:index'))
    else:
        messages.success(request,"Successful")
        request.session['emailid'] = result['user'].emailid
        request.session['name'] = result['user'].name
        request.session['userid'] = result['user'].id
        print result['user'].emailid
        return redirect(reverse('quotes:index')) 

def logout(request):
    request.session.clear()
    return redirect('auth:index')