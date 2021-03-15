from django.contrib import admin

# Register your models here.
from human_digita.action.models import Action


# one must have registered admin to have the add button on its related model
from human_digita.debatable.admin_forms import DebatableForm
from human_digita.debatable.models import Debatable


@admin.register(Debatable)
class DebatableAdmin(admin.ModelAdmin):
    search_fields = ['sentence_raw']
    form = DebatableForm
    exclude = ['activate_date', 'deactivate_date']

