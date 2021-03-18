from django.urls import reverse
from django.utils.safestring import mark_safe

from human_digita.archive_item.models import ArchiveItem


def get_archive_item_admin_link(doc: ArchiveItem):
    display_text = "<a href={}>{}</a>".format(
        reverse('admin:{}_{}_change'.format(doc._meta.app_label, doc._meta.model_name),
                args=(doc.pk,)),
        doc.title)
    if display_text:
        return mark_safe(display_text)
    return "-"
