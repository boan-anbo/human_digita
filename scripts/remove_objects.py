from django.contrib.contenttypes.models import ContentType

from human_digita.annotation.models import Annotation
from human_digita.common.const import LanguageTypes
from human_digita.passage.models import Passage
from util_functions.detect_language import detect_language


def run():
    ContentType.objects.all().delete()
