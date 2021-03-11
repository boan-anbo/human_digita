from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers

from human_digita.passage.models import Passage
from human_digita.passage.search_indexes import PassageIndex


class PassageSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Passage


class PassageIndexSerializer(HaystackSerializer):
    class Meta:
        index_classes = [PassageIndex]  # 索引类的名称
        fields = ['text', 'id']  # text 由索引类进行返回, object 由序列化类进行返回,第一个参数必须是text

