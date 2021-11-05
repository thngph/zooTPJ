from django.db import models
from home.models import Profile


# Create your models here.

class Ticket(models.Model):
    ticketID = models.AutoField(unique=True, primary_key=True)
    date_purchased = models.DateTimeField(auto_now_add=True)
    ticket_type = models.CharField(max_length=100)
    # need modify here
    price = models.IntegerField(blank=False)
    user_ID = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
