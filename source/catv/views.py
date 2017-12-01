from django.views.generic import ListView, DetailView

from catv.models import Video


class VideoListView(ListView):
    model = Video
    ordering = ['part']


class VideoDetailView(DetailView):
    model = Video
