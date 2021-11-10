from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Donate
from home.models import Profile
from django.http import HttpResponseRedirect
from rest_framework.status import HTTP_200_OK
from .serializers import DonateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
# Create your views here.
from home.forms import RegistrationForm
from django.http import JsonResponse

import stripe

stripe.api_key = "sk_test_51Jtlh9EiJAngkF1R6wywckuD1gOYyieoOBqg4EaP2STpe8GYoMp0iDTNpjBF1PeCUxbMkGQaxt8djtqOmjxfuTzG00yk4bAExN"


def index(request):
    if request.user.id:
        return render(request, 'donate/donate.html')
    else:
        return redirect('/login/')


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
            description="Donation"
        )
        user = User.objects.get(id=request.user.id)
        donation = Donate(amount=amount, user_ID=user)
        donation.save()

    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'donate/success.html', {'amount': amount})


# Donate API
class DonateAPI(APIView):
    def get(self, request, *arg, **kwargs):
        ObjDonate = Donate.objects.all()
        serializer = DonateSerializer(ObjDonate, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = DonateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
