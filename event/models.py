from django.db import models


# Create your models here.

class Event(models.Model):
    event_ID = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000)
    img = models.ImageField(default="", upload_to="photos/news")
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)