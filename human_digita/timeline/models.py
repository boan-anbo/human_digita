import uuid

from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.project.models import Project


class Timeline(TimeStampedModel, ActivatorModel, models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default='')
    name_cn = models.CharField(max_length=255, default='', blank=True)
    note = RichTextField(max_length=65535, default='', blank=True)
    projects = ManyToManyField(Project, related_name='timelines', blank=True)

    def __str__(self, short=True, plural=False):
        if short:
            return self.name
        else:
            return self.name + ' (' + self.note[0:20] + ')'
