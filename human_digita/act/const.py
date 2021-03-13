from django.db import models


class ActPropositionTypes(models.TextChoices):
    TO = 'TO', 'To'
    FOR = 'FOR', 'For'
    IN = 'IN', 'In'
