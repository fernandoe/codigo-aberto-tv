from django.db import models
from fe_core.base_models import UUIDModel


class Video(UUIDModel):
    identifier = models.IntegerField()
    youtube_video_id = models.CharField(max_length=20)
    title = models.CharField(max_length=120)
    part = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
