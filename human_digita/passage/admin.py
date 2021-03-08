from django.contrib import admin

# Register your models here.
from human_digita.passage.admin_forms import PassageForm
from human_digita.passage.models import Passage


@admin.register(Passage)
class PassageAdmin(admin.ModelAdmin):
    search_fields = ['text', 'before_text', 'after_text']
    list_display = ['text', 'before_text']
    form = PassageForm
    autocomplete_fields = ['location']
