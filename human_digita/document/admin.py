from django.contrib import admin

# Register your models here.
from human_digita.document.models import Document


@admin.register(Document)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'description']
