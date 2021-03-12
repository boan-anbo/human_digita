from django.db import models


class Importance(models.IntegerChoices):
    UNKNOWN = 0
    LOWEST = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    HIGHEST = 5

class LanguageTypes(models.TextChoices):
    UNKNOWN = 'UNKNOWN', 'Unknown'
    ENGLISH = 'ENGLISH', 'English'
    CHINESE = 'CHINESE', 'Chinese'
    OTHER = 'OTHER', 'Other'
