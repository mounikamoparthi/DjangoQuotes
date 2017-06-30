# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib import messages
from ..app_login.models import User
from .models import Quote
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    #Quote.objects.all().delete() 
    if not 'userid' in request.session:
        return redirect(reverse('auth:index'))
    current_user_id=User.objects.get(id=request.session['userid'])
    context = {
        'Userfav' :Quote.objects.all().filter(otherquotes=current_user_id),
        'Otheruserfavs' : Quote.objects.all().exclude(otherquotes=current_user_id),
        'Quotedata' :  Quote.objects.all(),
        "name":request.session['name'],
        "userid": request.session['userid']
    }
   
    return render(request,'app_quotes/index.html', context)

def addquotes(request):
    if not 'userid' in request.session:
        return redirect(reverse('auth:index'))
    if request.method == "POST":
        print request.POST
        context = {
                "name": request.session['name'],
                "userid" :  request.session['userid'] 
                }
        result = Quote.objects.addquotes(request.POST,context)
        if not result['status']:
             
            for error in result['errors']:
                messages.error(request,error)
                print "here"
            return redirect(reverse('quotes:index'))
        else: 
            messages.success(request,"Successful")
            return redirect(reverse('quotes:index'))
            
    else:
        print "ENTERED GET"
        context = {
                'Quotedata' :  Quote.objects.all(),
                'name': request.session['name']    
             }
    return render(request,'app_quotes/index.html',context)

def details (request, id):
    context = {
        "name": request.session['name'],
        'quote': Quote.objects.get(id=id),
        'Quotedata' :  Quote.objects.all(),

        }
     
    return render(request,'app_quotes/details.html', context)

def favquote(request,id):   
    
    
    context = {
                "quoteid" :id,
                "userid" : request.session['userid'] ,
                "name": request.session['name'],
                
                
                
                }
    
    
    result = Quote.objects.favquote(context)
    if not result['status']:
            for error in result['errors']:
                messages.error(request,error)
                print "here"
            #return redirect(reverse('secrets:add_like',kwargs={'id': id}))
            return redirect(reverse('quotes:index'))
    else: 
            messages.success(request,"Successful")
            return redirect(reverse('quotes:index'))
   


def delete(request,id):
    try:
        quote=Quote.objects.get(id=id)
        quote.delete()
        return redirect(reverse('quotes:index'))
    except:
        return redirect(reverse('quotes:index'))