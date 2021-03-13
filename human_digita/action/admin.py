from django.contrib import admin

# Register your models here.
from human_digita.action.models import Action


# one must have registered admin to have the add button on its related model
@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    search_fields = ['name', 'note']
    exclude = ['activate_date', 'deactivate_date']

