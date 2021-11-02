from django.db import models

# Create your models here.


class User(models.Model):
    user_ID = models.AutoField(primary_key=True)
