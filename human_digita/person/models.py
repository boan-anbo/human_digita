import uuid

from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.db.models import ManyToManyField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.annotation.models import Annotation
from human_digita.passage.models import Passage
from util_functions.pinyin import name_to_pinyin


class Person(TimeStampedModel, ActivatorModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, blank=True, default='')
    middle_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=True, default='')
    last_name_cn = models.CharField(max_length=255, blank=True, default='')
    first_name_cn = models.CharField(max_length=255, blank=True, default='')
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    annotations = models.ManyToManyField(Annotation, blank=True, related_name='people')
    note = RichTextField(max_length=65535, blank=True, default='')

    def __str__(self):
        if self.first_name_cn is not None and self.last_name_cn is not None:
            return f"{self.last_name_cn}{self.first_name_cn}"
        if self.first_name is not None and self.last_name is not None:
            return f"{self.first_name} {self.last_name}"

@receiver(pre_save, sender=Person)
def fill_pinyin_if_empty(sender, instance: Person, **kwargs):
    lastname_cn = instance.last_name_cn
    firstname_cn = instance.first_name_cn
    if lastname_cn and len(instance.last_name) == 0:
        instance.last_name = name_to_pinyin(lastname_cn)
    if firstname_cn  and len(instance.first_name) == 0:
        instance.first_name = name_to_pinyin(firstname_cn)
