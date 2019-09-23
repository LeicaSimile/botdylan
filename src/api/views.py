from django.shortcuts import render
import lyricsgenius
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .constants import GENIUS_ACCESS_TOKEN

@api_view(["GET"])
def artist(request):
    genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)
    return Response(data=genius.get_artist(request.GET.get("id")))

@api_view(["GET"])
def song(request):
    genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)
    return Response(data=genius.get_song(request.GET.get("id")))

@api_view(["GET"])
def songs_by_artist(request):
    genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)
    artist = genius.search_artist(request.GET.get("artist"))
    return Response(data=[song.to_dict() for song in artist.songs])

@api_view(["GET"])
def generated_song(request):
    return
