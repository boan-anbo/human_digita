import uuid
from datetime import datetime

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.db.models import ManyToManyField
from model_utils.models import TimeStampedModel

from human_digita.comment.models import Comment
from human_digita.document.models import Document


class Annotation(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    marked_text = RichTextField(max_length=65535, blank=True)
    modified_date = models.DateTimeField(blank=True, null=True, default=datetime.now)
    annotation_type = models.CharField(max_length=255, blank=True)
    page_index = models.IntegerField(null=True,blank=True)
    document = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True, blank=True, related_name='annotations')
    image = models.ImageField(blank=True)
    comments = ManyToManyField(Comment, 'annotations')

    def __str__(self):
        return self.marked_text
