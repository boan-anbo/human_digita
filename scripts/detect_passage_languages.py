from human_digita.annotation.models import Annotation
from human_digita.common.const import LanguageTypes
from human_digita.passage.models import Passage
from util_functions.detect_language import detect_language


def run():
    passages = Passage.objects.all()
    for passage in passages:
        if passage.text:
            passage.language = detect_language(passage.text)
            if passage.language is not LanguageTypes.UNKNOWN:
                print('passage detected')
            passage.save()
