from human_digita.annotation.models import Annotation


def run():
    annots = Annotation.objects.all()
    for annot in annots:
        if annot.page_index is None:
            annot.page_index = 0
            annot.save()
