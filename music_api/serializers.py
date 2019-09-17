from .models import Music, Contributor, Source, Title
from rest_framework import serializers


class ContribSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ('name')


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('name')

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
    titles = TitleSerializer
    contributors = ContribSerializer
    providers = SourceSerializer
    class Meta:
        model = Music
        fields = ('iswc', 'contributors', 'titles', 'sources')
        depth = 1