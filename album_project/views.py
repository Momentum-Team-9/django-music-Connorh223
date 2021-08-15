from django.shortcuts import render, redirect, get_object_or_404
from .models import Albums, Tracks
from .forms import AlbumsForm
# from django.http import HttpResponse
# trying to troubleshoot^


# Create your views here.

#Is this function erronious?? 
def list_albums(request):
    albums = Albums.objects.all()
    return render(request, 'list_albums.html', {'albums': albums})

def add_album(request):
    form = None
    if request.method == 'GET':
        form = AlbumsForm()
    else:
        form = AlbumsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
            # need to make that first ^
    return render(request, "album_project/add_album.html", {"form": form})


def delete_album(request, pk):
    album = get_object_or_404(Albums, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')
        # need to make that first ^
    return render(request, "album_project/delete_album.html",
                {"album": album})


def edit_album(request, pk):
    album = get_object_or_404(Albums, pk=pk)
    form = None
    if request.method == 'GET':
        form = AlbumsForm(instance=album)
    else:
        form = AlbumsForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
            # need to make that first
    return render(request, "album_project/edit_album.html", {
        "form": form,
        "album": album
    })


