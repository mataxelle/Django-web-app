from django.contrib import admin
from listings.models import Brand

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_created')

admin.site.register(Brand, BandAdmin)
