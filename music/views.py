from django.shortcuts import render
from django.http import HttpResponse
from .models import Album

# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)


def detail(request, album_id):
    album = Album.objects.get(id = album_id)
    html = '<p>' + album.album_title + '</p>'
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2> <br>" + html)

    