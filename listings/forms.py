from django import forms
from listings.models import Brand, Listing

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        exclude = ('active', 'official_homepage')

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ('sold',)