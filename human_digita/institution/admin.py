from django.contrib import admin

# Register your models here.
from human_digita.institution.models import Institution


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    ordering = ['start_year', 'start_month', 'start_day', 'name']
    list_display = ['id', '__str__', 'year_month_day', 'note']
    def year_month_day(self, obj: Institution):
        year_month_day = []
        if obj.start_year:
            year_month_day.append(obj.start_year.__str__())
        if obj.start_month:
            year_month_day.append(obj.start_month.__str__())
        if obj.start_day:
            year_month_day.append(obj.start_day.__str__())
        year_month_day_str = '-'.join(year_month_day)
        return year_month_day_str

