import uuid

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.archive.const import ArchiveTypes
from human_digita.archive_item.const import ArchiveItemType


class Archive(TimeStampedModel, ActivatorModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=200, choices=ArchiveTypes.choices, default=ArchiveTypes.VIRTUAL_ARCHIVE)
    name = models.CharField(max_length=255, blank=False)
    nameCn = models.CharField(max_length=255, blank=False)
    description = RichTextField(max_length=65535, blank=True)


