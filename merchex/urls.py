"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brands/', views.brand_list, name='brand-list'),
    path('brands/<int:id>/', views.brand_detail, name='brand-detail'),
    path('brands/<int:id>/edit/', views.brand_edit, name='brand-edit'),
    path('brands/add/', views.brand_add, name='brand-add'),
    path('listings/', views.listing_list, name='listing-list'),
    path('listings/<int:id>/', views.listing_detail, name='listing-detail'),
    path('listings/<int:id>/edit/', views.listing_edit, name='listing-edit'),
    path('listings/add/', views.listing_add, name='listing-add'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('sent-email/', views.email_sent, name='email-sent'),
    path('', views.listings, name='home'),
]
