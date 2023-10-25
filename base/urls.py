from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('products/', views.products),
    path('products/<id>', views.products),
    path('customers/', views.customers),
    path('customers/<id>', views.customers)
]
