from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django !</h1>')

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Ceci est une page à propos !</p>')

def contact(request):
    return HttpResponse('<h1>Contact</h1> <p>Ceci est une page de contact !</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>Ceci est une page de liste d\'annonces !</p>')