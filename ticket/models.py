from django.db import models
from home.models import User


# Create your models here.

class Ticket(models.Model):
    ticketID = models.AutoField(unique=True, primary_key=True)
    date_purchased = models.DateTimeField(auto_now_add=True)
    ticket_type = models.CharField(max_length=1000)
    # need modify here
    price = models.IntegerField(blank=False)
    user_ID = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
