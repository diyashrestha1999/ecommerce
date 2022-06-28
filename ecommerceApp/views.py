from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from  django import forms
from .models import Vendor, Customer, Product, Order, OrderDetail, Shop, Category

# Create your views here.


class VendorForm(forms.Form):
    vendor_name=forms.CharField(label='Vendor Name', max_length=50)
    vendor_number=forms.IntegerField()
    
def index(request):
    if request.method=="POST":
        value=VendorForm(request.POST)
        if value.is_valid():
            clean_name=value.cleaned_data["vendor_name"]
            clean_number=value.cleaned_data["vendor_number"]
            
            Vendor.objects.create(vendor_name=clean_name,vendor_number=clean_number)
            
            return HttpResponseRedirect(reverse("main:list"))
    return render(request,"html/index.html",{"form":VendorForm()})


def displayVendorList(request):
    vendor_list=Vendor.objects.all()
    return render(request,"html/list.html",{"vendor_list":vendor_list})

def displayCustomerList(request):
    customer_list=Customer.objects.all()
    return render(request,"html/list.html",{"customer_list":customer_list})

def displayProductList(request):
    product_list=Product.objects.all()
    return render(request,"html/list.html",{"product_list":product_list})

def displayShopList(request):
    shop_list=Shop.objects.all()
    return render(request,"html/list.html",{"shop_list":shop_list})

def displayCategoryList(request):
    category_list=Category.objects.all()
    return render(request,"html/list.html",{"category_list":category_list})

def displayOrderList(request):
    order_list=Order.objects.all()
    return render(request,"html/list.html",{"order_list":order_list})

def displayOrderList(request):
    orderDetail_list=OrderDetail.objects.all()
    return render(request,"html/list.html",{"orderDetail_list":orderDetail_list})