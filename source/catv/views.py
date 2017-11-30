from django.views.generic import ListView, DetailView

from catv.models import Video


class VideoListView(ListView):
    model = Video


class VideoDetailView(DetailView):
    model = Video
