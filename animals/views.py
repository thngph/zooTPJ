from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from home.forms import RegistrationForm


def index(request):
    return render(request, 'animals/animal.html')

