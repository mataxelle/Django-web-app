from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Brand, Listing
from listings.forms import BrandForm, ListingForm, ContactForm

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

def brand_edit(request, id):
    brand = Brand.objects.get(id=id)

    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)

        if form.is_valid():
            form.save()
            return redirect('brand-detail', brand.id)
    else:
        form = BrandForm(instance=brand)
    return render(request, 'listings/brand/brand_edit.html', {'form' : form, 'brand' : brand})

def brand_delete(request, id):
    brand = Brand.objects.get(id=id)

    if request.method == 'POST':
        brand.delete()
        messages.success(request, 'La marque a bien été supprimée.')
        return redirect('brand-list')
    return render(request, 'listings/brand/brand_delete.html', {'brand' : brand})

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing/listing_list.html', {'listings' : listings})

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, 'listings/listing/listing_detail.html', {'listing' : listing})

def listing_add(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)

        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing/listing_add.html', {'form' : form})

def listing_edit(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)

        if form.is_valid():
            form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing/listing_edit.html', {'form' : form, 'listing' : listing})

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