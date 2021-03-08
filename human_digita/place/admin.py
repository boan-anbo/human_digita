from django.contrib import admin

# Register your models here.
from human_digita.place.models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['name', 'note']
