from django.db import models
from django.db import models
from django.contrib.auth.models import User
from rest_framework.views import APIView


# Product class
class Product(models.Model):
    name = models.CharField(max_length=10,null=True,blank=True)
    category = models.CharField(max_length=10,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
 
    def __str__(self):
           return self.name


# Customer class
class Customer(models.Model):
    name = models.CharField(max_length=10,null=True,blank=True)
    last = models.CharField(max_length=10,null=True,blank=True)
    city = models.CharField(max_length=10,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
 
    def __str__(self):
           return self.name,self.last
       

# Task class
class Task(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
   
    def __str__(self):
        return self.title