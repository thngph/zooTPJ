from django.db import models
from home.models import Profile


# Create your models here.

class Donate(models.Model):
    donation_ID = models.AutoField(unique=True, primary_key=True)
    date_donated = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(blank=False)
    user_ID = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
