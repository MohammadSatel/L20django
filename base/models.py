from django.db import models


# Product class
class Product(models.Model):
    name = models.CharField(max_length=10,null=True,blank=True)
    category = models.CharField(max_length=10,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['name','category','price']
 
    def __str__(self):
           return self.name


# Customer class
class Customer(models.Model):
    name = models.CharField(max_length=10,null=True,blank=True)
    last = models.CharField(max_length=10,null=True,blank=True)
    city = models.CharField(max_length=10,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['name','last','city']
 
    def __str__(self):
           return self.name,self.last