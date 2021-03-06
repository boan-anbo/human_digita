import uuid

from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.institution_type.models import InstitutionType
from human_digita.place.models import Place


# an abstract grouping of actors.
class Institution(TimeStampedModel, ActivatorModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=512, default='')
    name_cn = models.CharField(max_length=512, default='')
    places = ManyToManyField(Place, blank=True)
    types = ManyToManyField(InstitutionType, blank=True)
    start_year = models.IntegerField(null=True, blank=True)
    start_month = models.IntegerField(null=True, blank=True)
    start_day = models.IntegerField(null=True, blank=True)
    note = RichTextField(max_length=65535, default='', blank=True)

    def __str__(self):
        return self.name + ' ' + self.name_cn
