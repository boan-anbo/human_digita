import uuid

from ckeditor.fields import RichTextField
from django.db import models

from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.archive.models import Archive
from human_digita.archive_item.const import ArchiveItemType

# the archive entry entity. does not differentiate from, say, multiple articles within same collection. the collection will be one archive entry, while the articles are multiple sources.


class ArchiveItem(TimeStampedModel, ActivatorModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=200, choices=ArchiveItemType.choices, default=ArchiveItemType)


    # three ways to identify an entry: title, file path, or identifier
    key = models.CharField(max_length=2000, blank=True) # e.g. unique identifier in the archive, like Zotero id or unique archive index or absolute path.
    file_path = models.FilePathField(max_length=3000, blank=True)  # e.g. unique identifier in the archive, like Zotero id or unique archive index or absolute path.
    title = models.CharField(max_length=2000, blank=True)
    # description of the archive entry
    description = RichTextField(max_length=2000, blank=True)

    archive = models.ForeignKey(
        Archive,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="archive_items"
    )


