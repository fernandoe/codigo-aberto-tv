from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from catv.views import VideoListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^videos/', TemplateView.as_view(template_name='catv/videos.html')),

    url(r'^$', VideoListView.as_view(), name='video-list'),
]
