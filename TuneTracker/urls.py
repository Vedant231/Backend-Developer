# TuneTracker/urls.py
from django.urls import path
from .views import song_list, song_detail

urlpatterns = [
    path('songs/', song_list, name='song_list'),
    path('song/<int:pk>/', song_detail, name='song_detail'),
]