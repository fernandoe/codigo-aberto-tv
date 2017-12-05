from django.core.management.base import BaseCommand, CommandError

from catv.models import Video


class Command(BaseCommand):
    def handle(self, *args, **options):
        for video in Video.objects.all():
            video.slugify_url()
