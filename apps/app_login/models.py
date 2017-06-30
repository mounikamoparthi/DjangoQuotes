# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, postData):
            #print "in def1"
            results = {'status': True, 'errors': [],'user':None}
            if not postData['name'] or len(postData['name']) <3:
                #print "fname error"
                results['status'] = False
                results['errors'].append("Please enter valid name")
            elif not postData['name'].isalpha():
                results['status'] = False
                results['errors'].append("Please enter only letters")
           
            if not postData['username'] or len(postData['username']) <1:
                results['status'] = False
                results['errors'].append("Please enter Username")
        
            elif not postData['username'] or len(postData['username']) <3:
                results['status'] = False
                results['errors'].append("UserName should be atleast three characters long")
            if not postData['emailid'] or len(postData['emailid']) <3:
                results['status'] = False
                results['errors'].append("Please enter valid emailid")
            elif not EMAIL_REGEX.match(postData['emailid']):
                results['status'] = False
                results['errors'].append("Please enter valid emailid")
            if not postData['password'] or len(postData['password']) <8:
                results['status'] = False
                results['errors'].append("Password must be atleat 4 characters long")
            if postData['reenterpassword'] != postData['password']:
                results['status'] = False
                results['errors'].append("Passwords do not match")
            if not postData['dob'] or len(postData['dob']) <1:
                results['status'] = False
                results['errors'].append("Please enter DOB")
            if not results['status']:
                return results
            x = User.objects.filter(emailid = postData['emailid'])
            try:
                if x[0]:
                    results['errors'].append("User already exists")
                    results['status'] = False
            except:
                if results['status']:
                    password = postData['password'].encode() # to get from unicode to string
                    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
                    print hashed
                    y = User.objects.create(name=postData['name'], username=postData['username'],dob=postData['dob'], emailid=postData['emailid'], password=hashed)
                    y.save()
                    results['user'] = y
            return results

    def loginval(self, postData):
            results = {'status': True, 'errors': [],'user':None}
            if not postData['emailid'] or len(postData['emailid']) <3:
                results['status'] = False
                results['errors'].append("Please enter valid emailid")
            elif not EMAIL_REGEX.match(postData['emailid']):
                results['status'] = False
                results['errors'].append("Please enter valid emailid")
            if not postData['password'] or len(postData['password']) <4:
                results['status'] = False
                results['errors'].append("Password must be atleat 4 characters long")
            if results['status'] == True:
                x = User.objects.filter(emailid = postData['emailid'])
            #print x
            
                try:
                    if x[0]:
                        print "in################# "
                        print x[0].password
                        password = postData['password'].encode()
                        y = x[0].password.encode()
                        if bcrypt.hashpw(password,y) == y:
                            results['status'] = True
                            print ("*****It matches**********")
                            results['user'] = x[0]
                        else:
                            results['status'] =False
                            results['errors'].append("Invalid credentials")
                            print ("*****It doesnt match**********")
                except:
                    results['status'] =False
                    print "please regitser"
                    results['errors'].append("Please Register")
            return results

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    emailid = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 
    objects = UserManager()
    #users1
    #users
    #travellers
