import uuid

from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from model_utils.models import TimeStampedModel


class Keyterm(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    name_cn = models.CharField(max_length=255, blank=True)

    note = RichTextField(max_length=1000, blank=True)


    def __str__(self):
        name = self.name
        if self.name_cn:
            return name + ' (' + name + ')'
        else:
            return name
