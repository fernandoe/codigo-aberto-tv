from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import loader
from django.utils.text import slugify
from fe_core.base_models import UUIDModel


class Tag(UUIDModel):
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Playlist(UUIDModel):
    youtube_playlist_id = models.CharField(max_length=50)
    title = models.CharField(max_length=120)

    def videos(self):
        return Video.objects.filter(playlists=self).order_by('part')

    def __str__(self):
        return self.title


class Video(UUIDModel):
    identifier = models.IntegerField()
    youtube_video_id = models.CharField(max_length=20)
    title = models.CharField(max_length=120)
    part = models.IntegerField()
    description = models.TextField()
    playlists = models.ManyToManyField(Playlist, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    # script = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def slugify_url(self):
        self.slug = slugify('Parte {PART:02}: {TITLE}'.format(PART=self.part, TITLE=self.title))
        self.save()

    def get_tags(self):
        return ", ".join(self.tags.values_list('name', flat=True))

    def get_long_description(self):
        t = loader.get_template('catv/description/base.txt')
        c = {
            'video': self
        }
        return t.render(c)


@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    if created:
        instance.slugify_url()
