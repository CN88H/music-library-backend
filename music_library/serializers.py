from rest_framework import serializers
from .models import MusicLibary

class MusicLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicLibary
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'genre']