from django.contrib import admin

from .models import Video


@admin.register(Video)
class EnderecoModelAdmin(admin.ModelAdmin):
    search_fields = ['youtube_video_id', 'title', 'description']
    list_display = ['get_uuid', 'identifier', 'part', 'youtube_video_id', 'title']
