from django.contrib import admin
from .models import Product
from .models import Customer

# Register models
admin.site.register(Product)
admin.site.register(Customer)

