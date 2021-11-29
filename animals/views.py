from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from rest_framework.status import HTTP_200_OK

from home.models import Profile
from .serializers import AnimalSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Animal
from rest_framework.parsers import JSONParser
# Create your views here.
from home.forms import RegistrationForm


def index(request):
    if request.user.is_authenticated:
        data = {'Animals': Animal.objects.all(),
                'Profile': Profile.objects.get(user_ID=request.user.id)}
    else:
        data = {'Animals': Animal.objects.all()}
    return render(request, 'animals/animal.html', data)


# Animal API
class AnimalAPI(APIView):
    def get(self, request, *arg, **kwargs):
        ObjAnimal = Animal.objects.all()
        serializer = AnimalSerializer(ObjAnimal, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = AnimalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

