from django.db import models


class ActionPropositionTypes(models.TextChoices):
    TO = 'TO', 'To'
    FOR = 'FOR', 'For'
    IN = 'IN', 'In'
