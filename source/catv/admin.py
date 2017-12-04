from django.contrib import admin

from .models import Video, Playlist


@admin.register(Video)
class VideoModelAdmin(admin.ModelAdmin):
    search_fields = ['youtube_video_id', 'title', 'description']
    list_display = ['get_uuid', 'identifier', 'part', 'youtube_video_id', 'title']


@admin.register(Playlist)
class PlaylistModelAdmin(admin.ModelAdmin):
    search_fields = ['youtube_playlist_id', 'title']
    list_display = ['get_uuid', 'youtube_playlist_id', 'title']
