from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from catv.views import VideoListView, PlaylistListView, VideoDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^videos/$', TemplateView.as_view(template_name='catv/videos.html')),

    # url(r'^$', VideoListView.as_view(), name='video-list'),
    url(r'^$', PlaylistListView.as_view(), name='playlist-list'),
    # url(r'^playlists/$', PlaylistListView.as_view(), name='playlist-list'),
    # url(r'^videos/(?P<pk>.*)$', VideoDetailView.as_view(), name='video-detail'),
    url(r'^videos/(?P<slug>[-\w]+)/$', VideoDetailView.as_view(), name='video-detail'),
]
