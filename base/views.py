from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .models import Customer
from django.template import loader
from django.shortcuts import render 


# Display templates
def index(request):
    return render(request, "index.html")


# Products CRUD
@api_view(['GET','POST','PUT','DELETE'])
def products(request,id=-1):
    if request.method == 'GET':
        products=[]
        for x in Product.objects.all():
            products.append({"name":x.name,"category":x.category,"price":x.price})
        return Response(products)  
       
       
    if request.method == 'POST':
        data=request.data
        prod=Product.objects.create(name=data["name"],category=data["category"],price=data["price"])
        return Response({"done:success", "product added", prod.name})
    
    
    if request.method == 'DELETE':
        del_prod=Product.objects.filter(id=id)
        del_prod.delete()
        return Response({"done:success", "product removed"})
    
    
    if request.method == 'PUT':
        data=request.data
        upd_prod=Product.objects.filter(id=id)[0]
        upd_prod.name=data["name"]
        upd_prod.category=data["category"]
        upd_prod.price=data["price"]
        upd_prod.save()
        return Response({"done:success", "product updated", upd_prod.name})
    
    
    # Customers CRUD
@api_view(['GET','POST','PUT','DELETE'])
def customers(request,id=-1):
    if request.method == 'GET':
        Customers=[]
        for x in Customer.objects.all():
            Customers.append({"name":x.name,"last":x.last,"city":x.city})
        return Response(Customers)  
       
       
    if request.method == 'POST':
        data=request.data
        cust=Customer.objects.create(name=data["name"],last=data["last"],city=data["city"])
        return Response({"done:success", "customer added", cust.name})
    
    
    if request.method == 'DELETE':
        del_cust=Customer.objects.filter(id=id)
        del_cust.delete()
        return Response({"done:success", "customer removed"})
    
    
    if request.method == 'PUT':
        data=request.data
        upd_cust=Customer.objects.filter(id=id)[0]
        upd_cust.name=data["name"]
        upd_cust.last=data["last"]
        upd_cust.city=data["city"]
        upd_cust.save()
        return Response({"done:success", "customer updated", upd_cust.name})