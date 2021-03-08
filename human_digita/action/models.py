import uuid

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.db.models import ManyToManyField
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel
from timezone_field import TimeZoneField

from human_digita.action_type.models import ActionType
from human_digita.actor.models import Actor
from human_digita.event.models import Event
from human_digita.interpretation.models import Interpretation
from human_digita.narrative.models import Narrative
from human_digita.passage.models import Passage
from human_digita.place.models import Place



class Action(TimeStampedModel, ActivatorModel, models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # subject. e.g. Qian gives Zhu a book. Qian
    actants=ManyToManyField(Actor, related_name='as_actants')

    # place
    places=ManyToManyField(Place, related_name='actions', blank=True)

    # verb
    types = ManyToManyField(ActionType, related_name='actions')
    description = RichTextField(max_length=65535, blank=True)

    # primary object. e.g. Qian gives Zhu a book. BOOK.
    first_recipients = ManyToManyField(Actor, related_name='as_first_recipients')

    # secondary object. e.g. Qian gives Zhu a book. ZHU.
    second_recipients = ManyToManyField(Actor, related_name='as_second_recipients', blank=True)
    # my own or other's narratives. other's NARRATIVES. NARRATIVE differs from passages in that it gives a coherent narrative, while passages might be fragmentary factual informations.
    narratives = ManyToManyField(Narrative, blank=True)
    passages = ManyToManyField(Passage, blank=True)
    # interpretation differs from narratives in that it can be more than temporal rendering of what has happened. It could theorize etc.
    interpretations = ManyToManyField(Interpretation, blank=True)

    # start
    start_datetime_local = models.DateTimeField(blank=True, null=True)
    start_datetime_utc = models.DateTimeField(blank=True, null=True)
    start_datetime_local_timezone =  TimeZoneField(default='UTC', choices_display='WITH_GMT_OFFSET', blank=True)
    # end
    end_datetime_local = models.DateTimeField(blank=True, null=True)
    end_datetime_utc = models.DateTimeField(blank=True, null=True)
    end_datetime_local_timezone =  TimeZoneField(default='UTC', choices_display='WITH_GMT_OFFSET', blank=True)

    #sentence
    sentence = models.CharField(max_length=512, default='', blank=True)


    def __str__(self):
        return self.sentence
