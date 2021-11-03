from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from home.forms import RegistrationForm


def index(request):
    return render(request, 'donate/donate.html')
