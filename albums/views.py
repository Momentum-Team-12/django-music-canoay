from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView  # new
from django.urls import reverse_lazy  # new
from .models import Album
from .forms import AlbumForm

# Create your views here.

def album_home(request):
    albums = Album.objects.all()
    return render(request, "albums/album_home.html", 
                 {"albums": albums})

def view_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/view_album.html",       
                    {"album": album})

def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='album_home')

    return render(request, "albums/add_album.html",{"form": form})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='album_home')

    return render(request, "albums/edit_album.html", {
        "form": form,
        "album": album
    })

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='album_home')

    return render(request, "albums/delete_album.html",
                  {"album": album})
