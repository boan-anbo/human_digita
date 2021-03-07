from django.contrib import admin

# Register your models here.
from human_digita.action.admin_forms import ActionForm
from human_digita.action.models import Action



@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    search_fields = ['description']
    form = ActionForm
