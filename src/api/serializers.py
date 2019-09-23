from rest_framework import serializers

class ArtistSerializer(serializers.Serializer):
    artist_id = serializers.CharField()
    name = serializers.CharField()
    image_url = serializers.URLField()
    num_songs = serializers.IntegerField()

class SongSerializer(serializers.Serializer):
    title = serializers.CharField()
    album = serializers.CharField()
    year = serializers.CharField()
    lyrics = serializers.CharField()
    image = serializers.URLField()
    
