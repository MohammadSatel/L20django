from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product


def index(req):
    return JsonResponse('hello home', safe=False)


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