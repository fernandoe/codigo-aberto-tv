from django.conf.urls import url
from django.contrib import admin

from catv.views import VideoListView, PlaylistListView, VideoDetailView, TagsView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^videos/$', VideoListView.as_view(), name='video-list'),

    url(r'^$', PlaylistListView.as_view(), name='playlist-list'),
    # url(r'^playlists/$', PlaylistListView.as_view(), name='playlist-list'),
    # url(r'^videos/(?P<pk>.*)$', VideoDetailView.as_view(), name='video-detail'),
    url(r'^videos/(?P<slug>[-\w]+)/$', VideoDetailView.as_view(), name='video-detail'),
    url(r'^tags$', TagsView.as_view(), name='tags'),
]
