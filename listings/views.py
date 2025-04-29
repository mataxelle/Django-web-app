from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Brand, Listing

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'listings/brand/brand_list.html', {'brands' : brands})

def brand_detail(request, id):
    brand = Brand.objects.get(id=id)
    return render(request, 'listings/brand/brand_detail.html', {'brand' : brand})

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing/listing_list.html', {'listings' : listings})

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, 'listings/listing/listing_detail.html', {'listing' : listing})

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')

def listings(request):
    brands = Brand.objects.all()
    return render(request, 'listings/listings.html', {'brands' : brands})