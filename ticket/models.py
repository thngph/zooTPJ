from django.conf import settings
from django.db import models
from home.models import Profile


# Create your models here.

class Ticket(models.Model):
    ticketID = models.AutoField(unique=True, primary_key=True)
    date_purchased = models.DateTimeField(auto_now_add=True)
    TICKET_CHOICES = (
        ('A', 'Adult'),
        ('C', 'Children'),
    )
    ticket_type = models.CharField(max_length=1, choices=TICKET_CHOICES, default='A')
    # need modify here
    price = models.IntegerField(blank=False)
    user_ID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.ticketID
