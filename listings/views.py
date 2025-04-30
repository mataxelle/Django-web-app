from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Brand, Listing
from listings.forms import BrandForm, ContactForm

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'listings/brand/brand_list.html', {'brands' : brands})

def brand_detail(request, id):
    brand = Brand.objects.get(id=id)
    return render(request, 'listings/brand/brand_detail.html', {'brand' : brand})

def brand_add(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)

        if form.is_valid():
            brand = form.save()
            return redirect('brand-detail', brand.id)
    else:
        form = BrandForm()
    return render(request, 'listings/brand/brand_add.html', {'form' : form})

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing/listing_list.html', {'listings' : listings})

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, 'listings/listing/listing_detail.html', {'listing' : listing})

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data['name'] or "anonyme"} via Merchex Contact us Form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['adminTest@merchex.com'],
            )
        return redirect('email-sent')
    else:
        form = ContactForm()
    return render(request, 'listings/contact.html', {'form' : form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')

def listings(request):
    brands = Brand.objects.all()
    return render(request, 'listings/listings.html', {'brands' : brands})