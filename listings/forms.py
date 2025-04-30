from django import forms
from listings.models import Brand

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'