from django.contrib import admin
from listings.models import Brand, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_created')

admin.site.register(Brand, BandAdmin)
admin.site.register(Listing)