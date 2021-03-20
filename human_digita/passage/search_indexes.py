from haystack import indexes

from human_digita.passage.models import Passage


class PassageIndex(indexes.SearchIndex, indexes.Indexable):
    # title = indexes.CharField()
    id = indexes.CharField(indexed=False)

    language = indexes.CharField(model_attr='language', null=True)

    title = indexes.CharField(indexed=True)

    document_id = indexes.CharField(indexed=True)

    text = indexes.CharField(document=True, model_attr='text')

    page_index = indexes.IntegerField(model_attr='page_index', null=True)

    last_used = indexes.DateTimeField(model_attr='last_used', null=True)

    annotations_count = indexes.IntegerField(indexed=True)




    def get_model(self):
        """返回建立索引的模型类"""
        return Passage

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.all()

    def prepare_id(self, obj):
        return obj.id

    def prepare_document_id(self, obj):
        document_id = None
        if obj.document:
            document_id = obj.document.id

        return document_id
    def prepare_title(self, obj: Passage):
        document_title=None
        if obj.document:
            document_title = obj.document.__str__()
        return document_title

    def prepare_annotations_count(self, obj: Passage):
        if obj.annotations.exists():
            return obj.annotations.count()
        else:
            return 0
    # def prepare_text(self, obj):
    #     return obj.marked_text
