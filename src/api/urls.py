from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('v1/artist', views.artist, name="artist"),
    path('v1/songs', views.songs_by_artist, name="songs_by_artist")
]
