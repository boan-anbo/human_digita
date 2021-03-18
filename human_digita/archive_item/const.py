from django.db import models


class ArchiveItemTypes(models.TextChoices):
    FILE = 'FILE', 'File'
    DOCUMENT = 'DOCUMENT', 'Document'
    IMAGE = 'IMAGE', "Image"


class ArchiveItemKeyTypes(models.TextChoices):
    CITE_KEY = 'CITE_KEY', 'Cite Key'
    URL = 'URL', 'Url'
