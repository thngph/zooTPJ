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
import stripe

stripe.api_key = "sk_test_51Jtlh9EiJAngkF1R6wywckuD1gOYyieoOBqg4EaP2STpe8GYoMp0iDTNpjBF1PeCUxbMkGQaxt8djtqOmjxfuTzG00yk4bAExN"


def index(request):
    if request.user.is_authenticated:
        data = {'Profile': Profile.objects.get(user_ID=request.user.id)}
        return render(request, 'ticket/ticket.html', data)
    else:
        return redirect('/login/')


def charge(request):
    amount = 0
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['adult_type_quantity'])*10 + int(request.POST['children_type_quantity'])*5

        customer = stripe.Customer.create(
            email=None or request.user.email,
            name=request.user.username,
            source=request.POST['stripeToken']
        )
        #
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency='usd',
            description="Ticket Payment"
        )
        user = None
        if request.user:
            user = User.objects.get(id=request.user.id)
        payment = Ticket(
            amount=amount,
            adult_type_quantity=request.POST['adult_type_quantity'],
            children_type_quantity=request.POST['children_type_quantity'],
            expired=request.POST['expired_in'],
            user_ID=user,
            )
        payment.save()

    return redirect(reverse('ticket_success', args=[amount]))


def successMsg(request, args):
    amount = args
    data = {
        'Profile': Profile.objects.get(user_ID=request.user.id),
        'amount': amount
    }
    return render(request, 'ticket/success.html', data)


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
