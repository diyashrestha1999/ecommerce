
from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor_name=models.CharField(max_length=50)
    vendor_number=models.IntegerField()
    
    def __str__(self):
        return f"Name: {self.vendor_name}, Number: {self.vendor_number}"
    
class Shop(models.Model):
    shop_name=models.CharField(max_length=50)
    shop_owner=models.ForeignKey(Vendor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Shop Name: {self.shop_name}, Owner: {self.shop_owner}"

class Category(models.Model):
    category_name=models.CharField(max_length=50)
    
    def __str__(self):
        return f"Category: {self.category_name}"
      
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_description=models.CharField(max_length=1000)
    shop=models.ManyToManyField(Shop)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Product Name: {self.product_name}, Description: {self.product_description}, Shop: {self.shop}, {self.category}"
    
class Customer(models.Model):
    customer_name=models.CharField(max_length=100)
    customer_username=models.CharField(max_length=50)
    customer_password=models.CharField(max_length=50)
    customer_email=models.EmailField()
    
    def __Str__(self):
        return f"Name: {self.customer_name}, Username:{self.customer_username}, Email:{self.customer_email}"
    
class Order(models.Model):
    order_date=models.DateField()
    pricing=models.FloatField()
    deliver_date=models.DateField()
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Order Date:{self.order_date}, Pricing: {self.pricing}, Deliver Date: {self.deliver_dat}, Ordered by:{self.customer}"
    
class OrderDetail(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Product Id: {self.product}, Order Id: {self.order}"
   