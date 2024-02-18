from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.


def home(request):
   info = CompanyInformation.objects.first()
   products = Product.objects.all()
   
   data ={
      
      'info':info,
      'products':products
   }
   
   return render(request, 'home.html',)

def about(request):
   return render(request, 'about.html')

def contact(request):
   return render(request, 'contact.html')

def product(request):
    info = CompanyInformation.objects.first()
    products = Product.objects.all()
   
    data ={
      
      'info':info,
      'products':products
   }
    return render(request, 'product.html',data)