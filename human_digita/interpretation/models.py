import uuid

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel


class Interpretation(TimeStampedModel, ActivatorModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    content = RichTextField(max_length=65535)
