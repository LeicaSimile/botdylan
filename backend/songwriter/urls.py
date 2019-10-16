from django.urls import path, include
from . import views

app_name = 'songwriter'

urlpatterns = [
    path('', views.songwriter, name="songwriter")
]
