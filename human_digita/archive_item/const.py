from django.db import models


class ArchiveItemType(models.TextChoices):
    File = 'FILE', 'File'
    Document = 'DOCUMENT', 'Document'
