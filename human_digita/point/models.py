import uuid

from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.annotation.models import Annotation
from human_digita.common.const import Importance
from human_digita.opinion.models import Opinion
from human_digita.project.models import Project


class Point(TimeStampedModel, ActivatorModel, models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    # in the form of STATEMENT: A is B or JUDGMENT: A should BE B
    name = models.CharField(max_length=255)
    gist = models.CharField(max_length=1024, blank=True)
    target = models.IntegerField(default=0, blank=True)
    index = models.IntegerField(default=0, blank=True)

    parent = models.ForeignKey('self', blank=True, related_name='children', null=True, on_delete=models.SET_NULL)
    annotations = ManyToManyField(Annotation, blank=True, related_name='points')
    manuscript = models.CharField(max_length=1024, blank=True)
    importance = models.IntegerField(choices=Importance.choices, default=Importance.UNKNOWN, blank=True)
    note = RichTextField(max_length=65535, blank=True, default='')

    # complications could be more nuanced and deserves future models to approximate the complexity of debates in reality.
    projects = ManyToManyField(Project, related_name='points', blank=True)


    def __str__(self, short=False, plural=False):
        return self.name
  #
  # id = v4();
  # name: string;
  # gist?: string = '';
  # note?: string = '';
  # target?: number = 0;
  # index?: number = 0;
  # type?: PointType = PointType.POINT;
  # children?: PointNew [];
  # annotations: StandardAnnotationFormat[] = [];
  # created?: Date;
  # modified?: Date;
