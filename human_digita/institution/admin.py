from django.contrib import admin

# Register your models here.
from human_digita.institution.models import Institution


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    ordering = ['name']
