from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=10,null=True,blank=True)
    category = models.CharField(max_length=10,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['name','category','price']
 
    def __str__(self):
           return self.name
