import uuid

from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.opinion.models import Opinion
from human_digita.project.models import Project


class Question(TimeStampedModel, ActivatorModel, models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # in the form of STATEMENT: A is B or JUDGMENT: A should BE B
    name = models.CharField(max_length=255)
    note = RichTextField(max_length=65535, blank=True, default='')
    # complications could be more nuanced and deserves future models to approximate the complexity of debates in reality.
    projects = ManyToManyField(Project, related_name='questions', blank=True)

    def __str__(self, short=False, plural=False):
        return self.name
