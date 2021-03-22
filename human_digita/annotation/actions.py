import base64

from django.core.files.base import ContentFile

from human_digita.annotation.models import Annotation
from human_digita.comment.actions import save_comment
from human_digita.document.models import Document
from human_digita.passage.models import Passage


def base64_to_imagefield_content(base64_str) -> ContentFile:
    # format, imgstr = base64_str.split(';base64,')  # format ~= data:image/X,
    # ext = format.split('/')[-1]  # guess file extension

    base64_str = ContentFile(base64.b64decode(base64_str), name='temp.' + 'png')
    return base64_str

def base65str_to_image_bytes(base65_str: str) -> bytes:
    image_data = base64.b64decode(base65_str)
    # fh.write(image_data)
    return image_data

# if there is old annotation, return it, otherwise return false
def check_duplicate_annotation(new_annot: Annotation):
    try:
        old_annots = Annotation.objects.filter(modified_date=new_annot.modified_date)
        if old_annots.exists():
            return old_annots[0]
        else:
            raise
    except:
        return False

# if update, missing fields will be added
def save_annotation(annotation_json, document: Document=None, update=True) -> str:
    try:
        new_annotation = Annotation()

        annotation_id = annotation_json.get('id', None)

        if annotation_id:
            old_annotation = Annotation.objects.get(pk=annotation_id)
            new_annotation = old_annotation

        # save image
        image_base64 = annotation_json.get('image', None)
        if image_base64:
            print('Found image base64')
            new_annotation.image = base64_to_imagefield_content(image_base64)

        # pageIndex
        page_index = annotation_json.get('pageIndex', None)
        if page_index is not None:
            new_annotation.page_index = page_index

        marked_text = annotation_json.get('markedText', None)
        if marked_text:
            new_annotation.marked_text = marked_text

        keyterms_raw = annotation_json.get('keyTermsRaw', None)
        if keyterms_raw:
            if new_annotation.keyterms_raw and len(new_annotation) > 0:
                new_annotation.keyterms_raw = new_annotation.keyterms_raw + ', ' + keyterms_raw
            else:
                new_annotation.keyterms_raw = keyterms_raw

        modified_date = annotation_json.get('modifiedDate', None)
        if modified_date:
            new_annotation.modified_date = modified_date

        # annotation type

        # annotation_type = annotation_json.get('annotationType', None)
        # if annotation_type:
        #     new_annotation.annotation_type = annotation_type

        # importance:
        importance = annotation_json.get('importance', None)
        if importance:
            new_annotation.importance = importance

        new_annotation.document = document

        old_annot = check_duplicate_annotation(new_annotation)
        if old_annot is not False:
            if update:
                if old_annot.document is None:
                    old_annot.document = document
                    old_annot.save()

        new_annotation.save()

        passage_json = annotation_json.get('passage', None)
        if passage_json:
            passage_id = passage_json.get('id', None)
            passage_obj = Passage.objects.get(id=passage_id)
            passage_obj.annotations.add(new_annotation)
            if new_annotation.document is None and passage_obj.document is not None:
                new_annotation.document = passage_obj.document
                new_annotation.save()
            passage_obj.save()

            # new_annotation.save()


        new_comments = annotation_json.get('comments', None)
        if new_comments:
            if annotation_id:

                for old_comment in new_annotation.comments.all():
                    isInNewComments = False
                    for new_comment in new_comments:
                        new_comment_id = new_comment.get('id', None)
                        if old_comment.id == new_comment_id:
                            isInNewComments = True
                    if isInNewComments is False:
                        old_comment.delete()
            for new_comment in new_comments:
                save_comment(new_comment, new_annotation)
        else:
            if annotation_id:
                for old_comment in new_annotation.comments.all():
                    old_comment.delete()
        return new_annotation.id
    except Exception as e:
        print("Save Annotation Error: ", e)
        raise
