from django.urls import path, include
from . import views

urlpatterns = [
    path('v1/artist', views.artist, name="artist")
]
