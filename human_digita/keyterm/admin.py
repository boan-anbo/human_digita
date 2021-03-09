from django.contrib import admin

# Register your models here.
from human_digita.keyterm.models import Keyterm


@admin.register(Keyterm)
class KeyTermAdmin(admin.ModelAdmin):
    search_fields = ['name', 'name_cn']
    list_display = ['id', 'name', 'name_cn']
    # form = PassageForm
    # autocomplete_fields = ['location']
