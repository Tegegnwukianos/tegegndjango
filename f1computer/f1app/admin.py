from django.contrib import admin
from .models import Product, Catagory, Brand

# Register your models here.
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Catagory)
