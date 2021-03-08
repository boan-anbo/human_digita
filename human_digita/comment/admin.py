from django.contrib import admin

# Register your models here.
from human_digita.comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    ordering = ['-created']
    search_fields = ['content']
