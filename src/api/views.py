from django.shortcuts import render
import lyricsgenius
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .constants import GENIUS_ACCESS_TOKEN

@api_view(["GET"])
def artist(request):
    return

@api_view(["GET"])
def song(request):
    return

@api_view(["GET"])
def songs_by_artist(request):
    genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)
    artist = genius.search_artist(request.GET.get("artist"))
    return Response(data=[song.to_dict() for song in artist.songs])

@api_view(["GET"])
def lyrics(request):
    return

@api_view(["GET"])
def lyrics_by_artist(request):
    return

