from django.contrib import admin

# Register your models here.
from human_digita.action_type.models import ActionType


# one must have registered admin to have the add button on its related model
@admin.register(ActionType)
class ActionTypeAdmin(admin.ModelAdmin):
    search_fields = ['name', 'note']
    exclude = ['activate_date', 'deactivate_date']

