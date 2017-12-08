from django.db.models import Count
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView

from catv.models import Video, Playlist, Tag


class VideoListView(ListView):
    model = Video

    def get_queryset(self):
        tag = self.request.GET.get('tag')
        qs = Video.objects.all()
        if tag is not None:
            qs = qs.filter(tags__name=tag)
        return qs.distinct().order_by('playlists', 'part')


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
                "link": '{URL}?tag={TAG}'.format(URL=reverse('video-list'), TAG=tag.name)
            })

        context['tags'] = output
        return context
