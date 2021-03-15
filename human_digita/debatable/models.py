import uuid

from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.opinion.models import Opinion
from human_digita.project.models import Project
from human_digita.topic.models import Topic


class Debatable(TimeStampedModel, ActivatorModel, models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # in the form of STATEMENT: A is B or JUDGMENT: A should BE B
    sentence_raw = models.CharField(max_length=255)
    note = RichTextField(max_length=65535, blank=True, default='')
    # that the debatable topic exists/is important
    acknowledges = ManyToManyField(Opinion, related_name='acknolwedge_debatables', blank=True)
    # that the topic is non-existent or non-debatable
    denials = ManyToManyField(Opinion, related_name='deny_debatables', blank=True)
    #
    supports = ManyToManyField(Opinion, related_name='support_debatables', blank=True)
    againsts = ManyToManyField(Opinion, related_name='against_debatables', blank=True)
    # complications could be more nuanced and deserves future models to approximate the complexity of debates in reality.
    neutrals = ManyToManyField(Opinion, related_name='complicate_debatables', blank=True)

    projects = ManyToManyField(Project, related_name='debatables', blank=True)
    topics = ManyToManyField(Topic, related_name='debatables', blank=True)

    def __str__(self, short=False, plural=False):
        return self.sentence_raw
