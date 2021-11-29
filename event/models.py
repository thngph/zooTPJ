from django.conf import settings
from django.db import models


# Create your models here.
from unidecode import unidecode

from home.models import Profile


def remove_accent(text):
    return unidecode(text)


class Event(models.Model):
    event_ID = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000)
    img = models.ImageField(default="", upload_to="photos/news")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    title_normalized = models.CharField(max_length=100, default='')
    description_normalized = models.CharField(max_length=1000, default='')

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.title_normalized = remove_accent(self.title)
        self.description_normalized = remove_accent(self.description)
        super(Event, self).save(*args, **kwargs)


class Comment(models.Model):
    comment_ID = models.AutoField(unique=True, primary_key=True)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        default=1
    )
    post = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        default=1
    )
    date_uploaded = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1000)
