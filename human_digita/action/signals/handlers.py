import logging

from django.db.models.signals import pre_save
from django.dispatch import receiver

from human_digita.action.models import Action
logger = logging.getLogger(__name__)

@receiver(pre_save, sender=Action)
def generate_action_sentence_en(sender, instance: Action, **kwargs):

    subject = ", ".join([
        child.__str__() for child in instance.actants.all()
    ])
    verbs = ", ".join([
        child.__str__(short=True) for child in instance.types.all()
    ])

    first_recipients = ", ".join([
        child.__str__() for child in instance.first_recipients.all()
    ])

    second_recipients = ", ".join([
        child.__str__() for child in instance.second_recipients.all()
    ])
    instance.sentence = subject + ' ' + verbs + ' ' + first_recipients + ' ' + second_recipients

    logger.info('Generated Sentence', instance.sentence)

