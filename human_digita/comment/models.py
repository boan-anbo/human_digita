import uuid

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.db.models import OneToOneField, ManyToManyField
from django_extensions.db.models import ActivatorModel, TimeStampedModel

from human_digita.passage.models import Passage


class Comment(TimeStampedModel,  models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = RichTextField(max_length=65535)

    passages =  ManyToManyField(Passage, 'comments')
    original = models.BooleanField(default=False)

    def __str__(self):
        return self.content
