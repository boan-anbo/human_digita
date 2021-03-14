from django.contrib import admin

# Register your models here.
from human_digita.act_type.models import ActType


# one must have registered admin to have the add button on its related model
from human_digita.timeline.admin_forms import TimelineForm
from human_digita.timeline.models import Timeline


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    search_fields = ['name', 'note']
    exclude = ['activate_date', 'deactivate_date']
    form = TimelineForm
