from django.contrib import admin

# one must have registered admin to have the add button on its related model
from human_digita.debatable.admin_forms import DebatableForm
from human_digita.debatable.models import Debatable


# Register your models here.


@admin.register(Debatable)
class DebatableAdmin(admin.ModelAdmin):
    search_fields = ['sentence_raw']
    form = DebatableForm
    exclude = ['activate_date', 'deactivate_date']

