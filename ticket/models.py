from datetime import datetime

from django.conf import settings
from django.db import models
from home.models import Profile


# Create your models here.

# More like Ticket Manager/Ticket Payment Model but its too late to re-name

class Ticket(models.Model):
    ticketID = models.AutoField(unique=True, primary_key=True)
    date_purchased = models.DateTimeField(auto_now_add=True)
    expired = models.DateField(blank=True)
    is_expired = models.BooleanField(default=False)
    adult_type_quantity = models.IntegerField(default=0)
    children_type_quantity = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    user_ID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return str(self.ticketID)


