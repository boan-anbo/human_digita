import uuid

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.archive_item.models import ArchiveItem
from human_digita.document.const import DocumentType


class Document(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=200, choices=DocumentType.choices, default=DocumentType.DOCUMENT)
    title = models.CharField(max_length=200, blank=False)
    description = RichTextField(max_length=65535, blank=True)
    content = RichTextField(max_length=65535, blank=True)
    archive_items = ManyToManyField(ArchiveItem, blank=True, related_name='documents')

    def __str__(self):
        return self.title
