from haystack import indexes

from human_digita.passage.models import Passage


class PassageIndex(indexes.SearchIndex, indexes.Indexable):
    # title = indexes.CharField()
    id = indexes.CharField(indexed=False)

    language = indexes.CharField(model_attr='language')

    title = indexes.CharField(indexed=True)

    text = indexes.CharField(document=True, model_attr='text')
    def get_model(self):
        """返回建立索引的模型类"""
        return Passage

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.all()

    def prepare_id(self, obj):
        return obj.id

    def prepare_title(self, obj: Passage):
        document_title=None
        if obj.document:
            document_title = obj.document.__str__()
        return document_title


    # def prepare_text(self, obj):
    #     return obj.marked_text
