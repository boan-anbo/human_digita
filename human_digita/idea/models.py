import uuid

from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.db.models import ManyToManyField
from model_utils.models import TimeStampedModel

# a seed. an idea to build upon.
from human_digita.keyterm.models import Keyterm


class Idea(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gist = models.CharField(max_length=225)
    notes = RichTextField(max_length=65535, blank=True)
    key_terms = ManyToManyField(Keyterm, related_name='ideas')
