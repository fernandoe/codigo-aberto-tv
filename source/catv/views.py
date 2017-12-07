from django.views.generic import ListView, DetailView, TemplateView

from catv.models import Video, Playlist, Tag
from django.db.models import Count


class VideoListView(ListView):
    model = Video
    ordering = ['part']


class PlaylistListView(ListView):
    model = Playlist


class VideoDetailView(DetailView):
    model = Video


class TagsView(TemplateView):
    template_name = "catv/tags.html"

    def get_context_data(self, **kwargs):
        context = super(TagsView, self).get_context_data(**kwargs)

        tags = Tag.objects.annotate(Count('video'))
        output = []
        for tag in tags:
            output.append({
                "text": tag.name,
                "weight": tag.video__count,
                "link": '/'
            })

        context['tags'] = output
        return context
