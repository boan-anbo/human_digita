from django.contrib import admin

# Register your models here.
from human_digita.person.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name', 'first_name_cn', 'last_name_cn']
