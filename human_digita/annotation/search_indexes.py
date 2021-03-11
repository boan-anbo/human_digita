from haystack import indexes

from human_digita.annotation.models import Annotation


class AnnotationIndex(indexes.SearchIndex, indexes.Indexable):
    # title = indexes.CharField()
    marked_text = indexes.CharField(model_attr='marked_text')
    id = indexes.CharField()

    text = indexes.CharField(document=True)
    def get_model(self):
        """返回建立索引的模型类"""
        return Annotation

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.all()
    def prepare_id(self, obj):
        return obj.id

    def prepare_text(self, obj):
        return obj.marked_text
