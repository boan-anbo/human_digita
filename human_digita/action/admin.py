from django.contrib import admin

# Register your models here.
from human_digita.action.admin_forms import ActionForm
from human_digita.action.models import Act

#
# class PassageInline(admin.TabularInline):
#     model = Action.passages.through
#     # form = PassageForm
#     show_change_link = True
#     # form = PassageForm

@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    search_fields = ['raw_sentence', 'sentence']
    form = ActionForm
    exclude = ['narratives', 'interpretations']


    def get_queryset(self, request):
        qs = super(ActAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('actants', 'passages')
        return qs
