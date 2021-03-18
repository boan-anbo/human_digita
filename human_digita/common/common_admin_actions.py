from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe


def get_image_previews(image_parents):
    previews = []
    for image_parent in image_parents:
        change_link = reverse('admin:{}_{}_change'.format(image_parent._meta.app_label, image_parent._meta.model_name),
                args=(image_parent.pk,))
        image_html = format_html('<a href={1}><img src="{0}" /></a>'.format(image_parent.image.url, change_link))
        if image_html:
            previews.append(image_html)
    if previews:
        return mark_safe(";<br>".join([
        child for child in previews
    ]))
    return '-'

  # display_text = "<a href={}>{}</a>".format(
  #       reverse('admin:{}_{}_change'.format(doc._meta.app_label, doc._meta.model_name),
  #               args=(doc.pk,)),
  #       doc.title)
#     display_text = "<a href={}>{}</a>".format(
#         reverse('admin:{}_{}_change'.format(comment._meta.app_label, comment._meta.model_name),
#                 args=(comment.pk,)),
#         comment.content)
#     if display_text:
#         links.append(display_text)
#
#
# if links:
#     return mark_safe(";<br>".join([
#         child for child in links
#     ]))
# return "-"
