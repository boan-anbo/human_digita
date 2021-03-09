import uuid

from django.db import models
# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.passage.models import Passage


class Person(TimeStampedModel, ActivatorModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, blank=False)
    first_name_cn = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    last_name_cn = models.CharField(max_length=255, blank=False)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    bio_passages = ManyToManyField(Passage, blank=True)

    def __str__(self):
        if self.first_name is not None and self.last_name is not None:
            return f"{self.first_name} {self.last_name}"
        if self.first_name_cn is not None and self.last_name_cn is not None:
            return f"{self.first_name_cn} {self.last_name_cn}"

