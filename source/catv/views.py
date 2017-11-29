from django.views.generic import ListView

from catv.models import Video


class VideoListView(ListView):
    model = Video

    # def get_context_data(self, **kwargs):
    #     context = super(ArticleListView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
