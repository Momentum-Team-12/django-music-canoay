from django.shortcuts import render
from .models import Album
from .forms import AlbumForm

# Create your views here.

def album_home(request):
    albums = Album.objects.all()
    return render(request, "albums/album_home.html", 
                  {"albums": albums})