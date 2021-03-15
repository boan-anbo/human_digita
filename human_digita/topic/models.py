import uuid

from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.knowledge_domain.models import KnowledgeDomain
from human_digita.project.models import Project


class Topic(TimeStampedModel, ActivatorModel, models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # in the form of STATEMENT: A is B or JUDGMENT: A should BE B
    name = models.CharField(max_length=255)
    note = RichTextField(max_length=65535, blank=True, default='')
    # complications could be more nuanced and deserves future models to approximate the complexity of debates in reality.
    projects = ManyToManyField(Project, related_name='topics', blank=True)
    knowledge_domains = ManyToManyField(KnowledgeDomain, related_name='topics', blank=True)

    def __str__(self, short=False, plural=False):
        return self.name
