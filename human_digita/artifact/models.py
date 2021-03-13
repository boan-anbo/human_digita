import uuid

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.annotation.models import Annotation
from human_digita.artifact_type.models import ArtifactType
from human_digita.project.models import Project


class Artifact(TimeStampedModel, ActivatorModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    name_cn = models.CharField(max_length=255, blank=True)
    projects = ManyToManyField(Project, related_name='artifacts', blank=True)
    artifact_types = ManyToManyField(ArtifactType, related_name='artifacts', blank=True)
    annotations = ManyToManyField(Annotation, related_name='annotations', blank=True)
    note = RichTextField(max_length=65535, default='', blank=True)

    def __str__(self):
        return self.name
