import uuid

from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.db.models import OneToOneField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.common.const import LanguageTypes
from human_digita.document.models import Document
from human_digita.event.models import Event
from human_digita.location.models import Location


class Passage(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    before_text = RichTextField(max_length=65535, blank=True)
    text = RichTextField(max_length=65535, blank=True)
    after_text = RichTextField(max_length=65535, blank=True)
    page_index = models.IntegerField(null=True,blank=True)
    # location = OneToOneField(Location, on_delete=models.SET_NULL, null=True, related_name='passage')
    document = models.ForeignKey(Document, blank=True, null=True, on_delete=models.CASCADE, related_name='passages')
    language = models.CharField(max_length=120, choices=LanguageTypes.choices, default=LanguageTypes.UNKNOWN)
    def __str__(self):
        return self.text[0:20]
