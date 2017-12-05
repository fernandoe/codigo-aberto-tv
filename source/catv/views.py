from django.views.generic import ListView, DetailView

from catv.models import Video, Playlist


class VideoListView(ListView):
    model = Video
    ordering = ['part']


class PlaylistListView(ListView):
    model = Playlist
    # ordering = ['part']


class VideoDetailView(DetailView):
    model = Video
