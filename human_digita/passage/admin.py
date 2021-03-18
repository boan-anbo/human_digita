from django.contrib import admin

# Register your models here.
from human_digita.common.common_admin_actions import get_image_previews
from human_digita.document.admin_actions import get_document_admin_link
from human_digita.passage.admin_forms import PassageForm
from human_digita.passage.models import Passage
# from human_digita.picture.admin_action import get_picture_admin_links
from human_digita.picture.admin_action import get_picture_admin_links


@admin.register(Passage)
class PassageAdmin(admin.ModelAdmin):
    search_fields = ['text', 'before_text', 'after_text']
    ordering = ['-created']
    list_filter = [
        'language',
    ]
    list_display = [
        'id',
        'page_index',
        'text',
        'document_link',
        'created',

    ]
    readonly_fields = [
        'id',
        'document_link',
        'picture_links',
        'picture_previews'
    ]
    form = PassageForm

    def get_queryset(self, request):
        qs = super(PassageAdmin, self).get_queryset(request)
        qs = qs.prefetch_related(
            'document',
            'pictures',
        )
        return qs

    def document_link(self, obj: Passage):
        doc = obj.document
        return get_document_admin_link(doc)

    def picture_links(self, obj: Passage):
        pictures = obj.pictures.all()
        return get_picture_admin_links(pictures)

    def picture_previews(self, obj: Passage):
        pictures = obj.pictures.all()
        image_parents = []
        for picture in pictures:
            image_parents.append(picture.archive_item)
        return get_image_previews(image_parents)

