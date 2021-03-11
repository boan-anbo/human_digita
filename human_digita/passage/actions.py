from human_digita.document.models import Document
from human_digita.location.models import Location
from human_digita.passage.models import Passage

def check_duplicate_passage(new_passage: Passage):
    try:
        old_passages = Passage.objects.filter(page_index=new_passage.page_index, text=new_passage.text, document=new_passage.document)
        if old_passages.exists():
            return old_passages[0]
        else:
            raise
    except:
        return False


def save_passage(passage_json, document: Document, update=True):


    newPassage = Passage()

    page_index = passage_json.get('pageIndex', None)
    if page_index is not None:
        newPassage.page_index = page_index

    text = passage_json.get('text', None)
    if text:
        newPassage.text = text

    newPassage.document = document

    old_passage = check_duplicate_passage(newPassage)
    if old_passage is not False:

        if update:
            if old_passage.document is None:
                old_passage.document = document
                old_passage.save()

        return

    newPassage.save()

    # comment = annotation_json.get('comment', None)
    # if comment:
    #     newComment: Comment = Comment()
    #     newComment.content = comment
    #     newComment.save()
    #     newComment.annotations.add(newAnnotation)
    #     newComment.save()
