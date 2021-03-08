from django.contrib import admin

# Register your models here.
from human_digita.location.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ['identifier', 'document__title']
    autocomplete_fields = ['document']
