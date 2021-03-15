from django.contrib import admin

# Register your models here.
from human_digita.action.models import Action


# one must have registered admin to have the add button on its related model
from human_digita.opinion.models import Opinion


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    search_fields = ['sentence_raw']
    exclude = ['activate_date', 'deactivate_date']

