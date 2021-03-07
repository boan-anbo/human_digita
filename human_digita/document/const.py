from django.db import models


class SourceType(models.TextChoices):
    DOCUMENT = 'DOCUMENT', 'Document' # languages
    WEB = 'WEB', 'Web' # humanities, sciences,
