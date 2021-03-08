from django.db import models


class DocumentType(models.TextChoices):
    DOCUMENT = 'DOCUMENT', 'Document' # languages
    WEB = 'WEB', 'Web' # humanities, sciences,
