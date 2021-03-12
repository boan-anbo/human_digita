from human_digita.annotation.models import Annotation
from human_digita.comment.models import Comment


def save_comment(comment_json, annotation: Annotation, update=True):


    new_comment: Comment = Comment()

    id = comment_json.get('id', None)
    if id:
        hasOldComment = Comment.objects.filter(id=id).exists()
        if hasOldComment:
            oldComment = Comment.objects.get(id=id)
            new_comment = oldComment

    new_comment.content = comment_json['content']
    new_comment.importance = comment_json['importance']

    # if id is None:
    new_comment.save()

    new_comment.annotations.add(annotation)
    new_comment.save()
