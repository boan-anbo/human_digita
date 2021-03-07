from django.db import models


class ArchiveTypes(models.TextChoices):
    PHYSICAL_ARCHIVE = 'PHYSICAL_ARCHIVE', 'Physical Archive'
    VIRTUAL_ARCHIVE = 'VIRTUAL_ARCHIVE', 'Virtual Archive' # internal built-in archive for human digita


