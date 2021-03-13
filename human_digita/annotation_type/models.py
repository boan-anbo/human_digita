import uuid

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel, ActivatorModel


class AnnotationType(TimeStampedModel, ActivatorModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, default='')
    note = RichTextField(max_length=2000, default='', blank=True)
