from django.urls import reverse
from django.utils.safestring import mark_safe

from human_digita.project.models import Project


def get_project_links(projects: [Project]) -> str:
    links = []
    for project in projects:
        display_text = "<a href={}>{}</a>".format(
            reverse('admin:{}_{}_change'.format(project._meta.app_label, project._meta.model_name),
                    args=(project.pk,)),
            project.__str__())
        if display_text:
            links.append(display_text)
    if links:
        return mark_safe("<br>".join([
            child for child in links
        ]))
    return "-"
