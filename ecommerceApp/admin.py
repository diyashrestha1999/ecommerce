from django.contrib import admin

# Register your models here.
from .models import Vendor, Shop, Category, Product,Customer, Order, OrderDetail

admin.site.register(Vendor)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderDetail)