import uuid

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.project.models import Project


class ArtifactType(TimeStampedModel, ActivatorModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    name_cn = models.CharField(max_length=255, blank=True)
    note = RichTextField(max_length=2000, default='', blank=True)

    def __str__(self):
        return self.name
