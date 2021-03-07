import uuid

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.document.models import Document
from human_digita.event.models import Event


class Passage(TimeStampedModel, ActivatorModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    before_text = RichTextField(max_length=65535, blank=True)
    text = RichTextField(max_length=65535, blank=True)
    after_text = RichTextField(max_length=65535, blank=True)
    events = ManyToManyField(Event, blank=True, related_name='passages')
    source_documents = ManyToManyField(Document, blank=True, related_name='passages')


