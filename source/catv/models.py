from django.db import models
from fe_core.base_models import UUIDModel


class Playlist(UUIDModel):
    youtube_playlist_id = models.CharField(max_length=50)
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Video(UUIDModel):
    identifier = models.IntegerField()
    youtube_video_id = models.CharField(max_length=20)
    title = models.CharField(max_length=120)
    part = models.IntegerField()
    description = models.TextField()
    playlists = models.ManyToManyField(Playlist, blank=True)
    # script = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
