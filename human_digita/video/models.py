import uuid

from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.db.models import ManyToManyField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.archive_item.models import ArchiveItem
from human_digita.common.const import Importance
from human_digita.project.models import Project


class Video(TimeStampedModel, ActivatorModel, models.Model):

    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # in the form of STATEMENT: A is B or JUDGMENT: A should BE B
    name = models.CharField(max_length=255, blank=True)
    note = RichTextField(max_length=65535, blank=True, default='')
    importance = models.IntegerField(choices=Importance.choices, default=Importance.UNKNOWN, blank=True)
    # complications could be more nuanced and deserves future models to approximate the complexity of debates in reality.
    projects = ManyToManyField(Project, related_name='videos', blank=True)
    source = models.CharField(max_length=512, blank=True)
    description = RichTextField(max_length=65535, blank=True)

    archive_item = models.ForeignKey(
        ArchiveItem,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='videos'
    )

    def __str__(self, short=False, plural=False):
        return self.name


@receiver(pre_save, sender=Video)
def use_archive_item_name_for_video_if_blank(sender, instance: Video, **kwargs):
    if instance.name is None or len(instance.name) == 0:
        archive_item = instance.archive_item
        if archive_item:
            instance.name = archive_item.title
