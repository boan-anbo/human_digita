import uuid

from ckeditor.fields import RichTextField
from django.db import models
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.archive.models import Archive
from human_digita.archive_item.const import ArchiveItemTypes, ArchiveItemKeyTypes


# the archive entry entity. does not differentiate from, say, multiple articles within same collection. the collection will be one archive entry, while the articles are multiple sources.

def get_file_name(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        return '{}.{}'.format(instance.__str__(), ext)
    else:
        pass


class ArchiveItem(TimeStampedModel, ActivatorModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=200, choices=ArchiveItemTypes.choices, default=ArchiveItemTypes.DOCUMENT)

    title = models.CharField(max_length=2000, blank=False)

    # three ways to identify an entry: title, file path, or identifier
    key = models.CharField(max_length=2000, blank=True) # e.g. unique identifier in the archive, like Zotero id or unique archive index or absolute path.
    key_type = models.CharField(max_length=200, choices=ArchiveItemKeyTypes.choices, default=ArchiveItemKeyTypes.CITE_KEY)
    file_path = models.CharField(max_length=3000, blank=True)
    file_url = models.CharField(max_length=3000, blank=True)
    file_name = models.CharField(max_length=1000, blank=True)
    # description of the archive entry
    description = RichTextField(max_length=2000, blank=True)

    file_modified_date = models.DateTimeField(blank=True, null=True)
    file_created_date = models.DateTimeField(blank=True, null=True)

    image = models.ImageField(blank=True, upload_to=get_file_name)

    file = models.FileField(blank=True, upload_to=get_file_name)

    note = RichTextField(max_length=65535, blank=True)


    archive = models.ForeignKey(
        Archive,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="archive_items"
    )


    def __str__(self):
        return self.title
