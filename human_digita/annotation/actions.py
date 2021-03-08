import base64

from django.core.files.base import ContentFile

from human_digita.annotation.models import Annotation
from human_digita.comment.models import Comment


def base64_to_imagefield_content(base64_str) -> ContentFile:
    # format, imgstr = base64_str.split(';base64,')  # format ~= data:image/X,
    # ext = format.split('/')[-1]  # guess file extension

    base64_str = ContentFile(base64.b64decode(base64_str), name='temp.' + 'png')
    return base64_str

def base65str_to_image_bytes(base65_str: str) -> bytes:
    image_data = base64.b64decode(base65_str)
    # fh.write(image_data)
    return image_data

def save_annotation(annotation_json):
    newAnnotation = Annotation()

    # save image
    image_base64 = annotation_json.get('image', None)
    if image_base64:
        print('Found image base64')
        newAnnotation.image = base64_to_imagefield_content(image_base64)


    # pageIndex
    page_index = annotation_json.get('pageIndex', None)
    if page_index:
        newAnnotation.page_index = page_index

    marked_text = annotation_json.get('markedText', None)
    if marked_text:
        newAnnotation.marked_text = marked_text

    modified_date = annotation_json.get('modifiedDate', None)
    if modified_date:
        newAnnotation.modified_date = modified_date

    annotation_type = annotation_json.get('annotationType', None)
    if annotation_type:
        newAnnotation.annotation_type = annotation_type



    newAnnotation.save()

    comment = annotation_json.get('comment', None)
    if comment:
        newComment: Comment = Comment()
        newComment.content = comment
        newComment.save()
        newComment.annotaions.add(newAnnotation)
        newComment.save()
