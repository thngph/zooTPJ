from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from home.forms import RegistrationForm


def index(request):
    return render(request, 'ticket/ticket.html')


def redirect_donate(request):
    return redirect('/donate/')
