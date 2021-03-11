from haystack import indexes

from human_digita.document.models import Document


class DocumentIndex(indexes.SearchIndex, indexes.Indexable):
    # title = indexes.CharField()
    title = indexes.CharField(model_attr='title')
    text = indexes.CharField(document=True)
    def get_model(self):
        """返回建立索引的模型类"""
        return Document

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.all()
