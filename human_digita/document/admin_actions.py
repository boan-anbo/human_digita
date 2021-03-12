from django.utils.safestring import mark_safe
from rest_framework.reverse import reverse

from human_digita.document.models import Document


def get_document_admin_link(doc: Document):
    display_text = "<a href={}>{}</a>".format(
        reverse('admin:{}_{}_change'.format(doc._meta.app_label, doc._meta.model_name),
                args=(doc.pk,)),
        doc.title)
    if display_text:
        return mark_safe(display_text)
    return "-"
