from django.db import models


class ActorEntityTypes(models.TextChoices):
    OBJECT = 'OBJECT', 'Object'
    PERSON = 'PERSON', 'Person'
    INSTITUTION = "INSTITUTION", "Institution"
    EVENT = 'EVENT', 'Event'


class ActorRoleTypes(models.TextChoices):
    ACTANT = 'ACTANT', 'Actant'
    RECIPIENT = 'RECIPIENT', 'Recipient'
