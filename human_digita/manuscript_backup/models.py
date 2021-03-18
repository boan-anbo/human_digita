import uuid

from django.db import models
# Create your models here.
from django_extensions.db.models import ActivatorModel
from jsonfield import JSONField
from model_utils.models import TimeStampedModel


class ManuscriptBackup(TimeStampedModel, ActivatorModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manuscript = JSONField()
    manuscript_id = models.UUIDField(blank=False, editable=True)


