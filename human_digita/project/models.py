import uuid

from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.keyterm.models import Keyterm


class Project( TimeStampedModel, ActivatorModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = RichTextField(max_length=65535, blank=True)
    keyterms = ManyToManyField(Keyterm, blank=True, related_name='projects')


    def __str__(self):
        return self.name
