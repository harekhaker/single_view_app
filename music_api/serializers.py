from .models import Music, Contributor, Provider
from rest_framework import serializers


class ContribSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ('name')


class ProvideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('name')

class MusicSerializer(serializers.ModelSerializer):
    contributors = ContribSerializer
    providers = ProvideSerializer
    class Meta:
        model = Music
        fields = ('iswc', 'contributors', 'song_name', 'providers')
        depth = 1