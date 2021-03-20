from django.urls import reverse
from django.utils.safestring import mark_safe



def get_video_admin_links(videos) -> str:
    links = []
    for video in videos:
        display_text = "<a href={}>{}</a>".format(
            reverse('admin:{}_{}_change'.format(video._meta.app_label, video._meta.model_name),
                    args=(video.pk,)),
            video.__str__())
        if display_text:
            links.append(display_text)
    if links:
        return mark_safe("<br>".join([
            child for child in links
        ]))
    return "-"
