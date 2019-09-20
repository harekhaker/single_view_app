from .models import Music, Contributor, Source, Title
from rest_framework import serializers


class ContribSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ('name',)

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('name',)


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('title', 'lang')

class MusicSerializer(serializers.ModelSerializer):
    titles = TitleSerializer(many=True, read_only=True)
    contributors = ContribSerializer(many=True, read_only=True)
    sources = SourceSerializer(many=True, read_only=True)

    class Meta:
        model = Music
        fields = ('iswc', 'contributors', 'titles', 'sources')


class MusicCSVSerializer(serializers.ModelSerializer):
    titles = TitleSerializer(many=True, read_only=True)
    contributors = ContribSerializer(many=True, read_only=True)
    sources = SourceSerializer(many=True, read_only=True)

    class Meta:
        model = Music
        fields = ('iswc', 'contributors', 'titles', 'sources')
