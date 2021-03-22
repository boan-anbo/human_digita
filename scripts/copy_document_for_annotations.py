from django.contrib.contenttypes.models import ContentType

from human_digita.annotation.models import Annotation
from human_digita.common.const import LanguageTypes
from human_digita.passage.models import Passage
from util_functions.detect_language import detect_language


def run():
    annotations = Annotation.objects.all()
    for annotation in annotations:
        if annotation.document is None and annotation.passage and annotation.passage.document is not None:
            annotation.document = annotation.passage.document
        annotation.save()
