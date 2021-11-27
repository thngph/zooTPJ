from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user_ID = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(default='new user', max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=15)
    img = models.ImageField(default='', upload_to="photos/user")
    objects = models.Manager()

    def __str__(self):
        return self.name



