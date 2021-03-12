from django.urls import reverse
from django.utils.safestring import mark_safe


def get_passage_links(passages) -> str:
    links = []
    for passage in passages:
        display_text = "<a href={}>{}</a>".format(
            reverse('admin:{}_{}_change'.format(passage._meta.app_label, passage._meta.model_name),
                    args=(passage.pk,)),
            passage.__str__())
        if display_text:
            links.append(display_text)
    if links:
        return mark_safe("<br>".join([
            child for child in links
        ]))
    return "-"
