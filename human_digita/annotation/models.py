import uuid
from datetime import datetime

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.db.models import ManyToManyField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.annotation_type.models import AnnotationType
from human_digita.comment.models import Comment
from human_digita.common.const import Importance
from human_digita.document.models import Document
from human_digita.keyterm.models import Keyterm
from human_digita.passage.models import Passage
from human_digita.project.models import Project


class Annotation(ActivatorModel, TimeStampedModel, models.Model):


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # core:
    marked_text = RichTextField(max_length=65535, blank=True)
    comments = ManyToManyField(Comment, related_name='annotations', blank=True)
    # important
    annotation_types = models.ManyToManyField(AnnotationType, blank=True, related_name='annotations')
    keyterms = ManyToManyField(Keyterm, related_name='annotations', blank=True)
    passage =  models.ForeignKey(Passage, related_name='annotations', blank=True, on_delete=models.SET_NULL, null=True)

    keyterms_raw = models.CharField(max_length=1024, blank=True, default='')
    time_raw = models.CharField(max_length=512, blank=True, default='')

    projects = ManyToManyField(Project, related_name='annotations', blank=True)
    importance = models.IntegerField(choices=Importance.choices, default=Importance.UNKNOWN, blank=True)
    document = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True, blank=True, related_name='annotations')

    modified_date = models.DateTimeField(blank=True, null=True, default=datetime.now)
    page_index = models.IntegerField(null=True,blank=True)

    image = models.ImageField(blank=True)



    def __str__(self):
        return self.marked_text[0:25]

