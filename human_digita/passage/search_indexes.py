from haystack import indexes

from human_digita.passage.models import Passage


class PassageIndex(indexes.SearchIndex, indexes.Indexable):
    # title = indexes.CharField()
    id = indexes.CharField(indexed=False)

    language = indexes.CharField(model_attr='language')

    text = indexes.CharField(document=True, model_attr='text')
    def get_model(self):
        """返回建立索引的模型类"""
        return Passage

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.all()

    def prepare_id(self, obj):
        return obj.id

    # def prepare_text(self, obj):
    #     return obj.marked_text
