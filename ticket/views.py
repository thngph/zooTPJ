import stripe
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from .serializers import TicketSerializer
from .models import Ticket
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
from home.forms import RegistrationForm


def index(request):
    return render(request, 'ticket/ticket.html')


def charge(request):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.user.username,
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency='usd',
            description="Ticket Payment"
        )
        user = User.objects.get(id=request.user.id)
        donation = Ticket(amount=amount, user_ID=user)
        donation.save()

    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'donate/success.html', {'amount': amount})


# Ticket API
class TicketAPI(APIView):
    def get(self, request, *arg, **kwargs):
        ObjTicket = Ticket.objects.all()
        serializer = TicketSerializer(ObjTicket, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = TicketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
