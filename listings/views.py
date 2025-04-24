from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Brand

def hello(request):
    brands = Brand.objects.all()
    return render(request, 'listings/hello.html', {'brands' : brands})

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')

def listings(request):
    brands = Brand.objects.all()
    return render(request, 'listings/listings.html', {'brands' : brands})