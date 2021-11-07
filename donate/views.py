from django.shortcuts import render, redirect
from .models import Donate
from django.http import HttpResponseRedirect
from rest_framework.status import HTTP_200_OK
from .serializers import DonateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
# Create your views here.
from home.forms import RegistrationForm


def index(request):
    return render(request, 'donate/donate.html')


def redirect_ticket(request):
    return redirect('/ticket/')


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
