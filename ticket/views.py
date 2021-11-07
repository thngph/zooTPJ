from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
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


def redirect_donate(request):
    return redirect('/donate/')


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
