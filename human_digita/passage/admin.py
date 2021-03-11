from dal_admin_filters import AutocompleteFilter
from django.contrib import admin

# Register your models here.
from human_digita.passage.admin_forms import PassageForm
from human_digita.passage.models import Passage

# class DocumentFilter(AutocompleteFilter):
#     title = 'Document Title'                    # filter's title
#     field_name = 'document'           # field name - ForeignKey to Country model
#     autocomplete_url = 'document-autocomplete' # url name of Country autocomplete view


@admin.register(Passage)
class PassageAdmin(admin.ModelAdmin):
    search_fields = ['text', 'before_text', 'after_text']
    list_filter = [
        'document'
    ]
    list_display = [
        'id',
        'page_index',
        'text',
        'document',
        'created',
    ]
    readonly_fields = ['id']
    form = PassageForm

    def get_queryset(self, request):
        qs = super(PassageAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('document')
        return qs



