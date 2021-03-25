import uuid

from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel
from timezone_field import TimeZoneField

from human_digita.act_type.models import ActType
from human_digita.action.models import Action
from human_digita.actor.models import Actor
from human_digita.annotation.models import Annotation
from human_digita.event.models import Event
from human_digita.interpretation.models import Interpretation
from human_digita.narrative.models import Narrative
from human_digita.passage.models import Passage
from human_digita.place.models import Place
from human_digita.timeline.models import Timeline


class Act(TimeStampedModel, ActivatorModel, models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # subject. e.g. Qian gives Zhu a book. Qian
    actants=ManyToManyField(Actor, related_name='as_actants', blank=True)

    sentence_raw = models.CharField(max_length=2046, default='', blank=False)
    keyterms_raw = models.CharField(max_length=1024, default='', blank=True)
    time_raw = models.CharField(max_length=256, default='', blank=True)



    start_year_local = models.IntegerField(blank=True, null=True)
    start_month_local = models.IntegerField(blank=True, null=True)
    start_day_local = models.IntegerField(blank=True, null=True)
    start_hour_local = models.IntegerField(blank=True, null=True)


    #type. e.g. timeline. bio.
    act_types = ManyToManyField(ActType, related_name='acts', blank=True)

    # place
    places=ManyToManyField(Place, related_name='acts', blank=True)

    ## place
    timelines=ManyToManyField(Timeline, related_name='acts', blank=True)

    # verb
    action = ManyToManyField(Action, related_name='acts', blank=True)
    description = RichTextField(max_length=65535, blank=True)

    # primary object. e.g. Qian gives Zhu a book. BOOK.
    first_recipients = ManyToManyField(Actor, related_name='as_first_recipients', blank=True)

    # secondary object. e.g. Qian gives Zhu a book. ZHU.
    second_recipients = ManyToManyField(Actor, related_name='as_second_recipients', blank=True)
    # my own or other's narratives. other's NARRATIVES. NARRATIVE differs from passages in that it gives a coherent narrative, while passages might be fragmentary factual informations.
    narratives = ManyToManyField(Narrative, blank=True)
    # passages = ManyToManyField(Passage, blank=True)
    annotations = ManyToManyField(Annotation, blank=True, related_name='acts')
    # interpretation differs from narratives in that it can be more than temporal rendering of what has happened. It could theorize etc.
    interpretations = ManyToManyField(Interpretation, blank=True)

    note = RichTextField(max_length=65535, blank=True, null=True)


    # start
    start_datetime_local = models.DateTimeField(blank=True, null=True)
    start_datetime_utc = models.DateTimeField(blank=True, null=True)
    start_datetime_local_timezone =  TimeZoneField(default='UTC', blank=True)
    # end
    end_datetime_local = models.DateTimeField(blank=True, null=True)
    end_datetime_utc = models.DateTimeField(blank=True, null=True)
    end_datetime_local_timezone =  TimeZoneField(default='UTC', blank=True)

    #sentence
    sentence = models.CharField(max_length=512, default='', blank=True)

    def __str__(self):
        sentence = ''
        if self.sentence:
            sentence = self.sentence
        else:
            sentence = self.sentence_raw
        return sentence
