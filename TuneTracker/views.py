from django.shortcuts import render
from .models import Song

def song_list(request):
    songs=Song.objects.all()
    return render(request,'TuneTracker/song_list.html',{'songs':songs})

def song_detail(request,pk):
    song=Song.objects.get(pk=pk)
    return render(request,'TuneTracker/song_detail.html',{'song':song})



# Create your views here.
