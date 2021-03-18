from django.urls import reverse
from django.utils.safestring import mark_safe



def get_picture_admin_links(pictures) -> str:
    links = []
    for picture in pictures:
        display_text = "<a href={}>{}</a>".format(
            reverse('admin:{}_{}_change'.format(picture._meta.app_label, picture._meta.model_name),
                    args=(picture.pk,)),
            picture.__str__())
        if display_text:
            links.append(display_text)
    if links:
        return mark_safe("<br>".join([
            child for child in links
        ]))
    return "-"
