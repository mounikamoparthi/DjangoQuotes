# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..app_login.models import User

from django.db import models

# Create your models here.
class QuoteManager(models.Manager):
    def addquotes(request,postData,sessiondata):
        print postData
        results = {'status': True, 'errors': []}
        if not postData['Quoted By'] or len(postData['Quoted By'])<3:
            print "In quotes "
            results['status'] = False
            results['errors'].append("Please enter a valid name")
        if not postData['message'] or len(postData['message'])<10:
            print "In quotes_messages "
            results['status'] = False
            results['errors'].append("Please enter a valid message")

        if results['status']:
            user1 = User.objects.get(id = sessiondata['userid'])
            Quote1 = Quote.objects.create(quotedby=postData['Quoted By'],
            message=postData['message'],userquotes = user1)
            print "ddfghjkl"
            results['status'] = True
            print "Successfully done!!!!!!!!!"
       
        return results    
    def favquote(request,context):
        print context
        results = {'status': True, 'errors': []}

        Quote2=Quote.objects.get(id=context["quoteid"])
        user1=User.objects.get(id=context["userid"])
    
        Quote2.otherquotes.add(user1)
        print "join done!!!!!!!!!"
        results['status'] = True
        return results 

class Quote(models.Model):
    quotedby = models.CharField(max_length=1000)
    message =  models.TextField(max_length=1000)
    userquotes= models.ForeignKey('app_login.User', related_name="userquotes")
    otherquotes = models.ManyToManyField('app_login.User', related_name="otherquotes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
     
    objects=QuoteManager()