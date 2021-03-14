from django.contrib import admin

# Register your models here.
from human_digita.act.admin_forms import ActForm
from human_digita.act.models import Act


#
# class PassageInline(admin.TabularInline):
#     model = Action.passages.through
#     # form = PassageForm
#     show_change_link = True
#     # form = PassageForm

@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    search_fields = ['raw_sentence', 'sentence']
    form = ActForm
    ordering = ['start_year_local', 'start_month_local', 'start_day_local']
    exclude = ['narratives', 'interpretations']
    list_display = ['__str__', 'keyterms_raw', 'year_month_day']


    def get_queryset(self, request):
        qs = super(ActAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('actants', 'annotations')
        return qs



    def year_month_day(self, obj: Act):
        year_month_day = []
        if obj.start_year_local:
            year_month_day.append(obj.start_year_local.__str__())
        if obj.start_month_local:
            year_month_day.append(obj.start_month_local.__str__())
        if obj.start_day_local:
            year_month_day.append(obj.start_day_local.__str__())
        year_month_day_str = '-'.join(year_month_day)
        return year_month_day_str
