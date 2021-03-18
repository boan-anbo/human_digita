import uuid

from django.db import models
# Create your models here.
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel


class InstitutionType(TimeStampedModel, ActivatorModel, models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    name_cn = models.CharField(max_length=255)
