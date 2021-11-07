from django.core.files.storage import FileSystemStorage
from django.db import models


# Create your models here.

class Animal(models.Model):
    animal_ID = models.AutoField(unique=True, primary_key=True)
    animal_name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=1000)
    img = models.ImageField(default="", upload_to="photos/animals")
    profile_img = models.ImageField(default="", upload_to="photos/animals")
