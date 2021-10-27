from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from home.forms import RegistrationForm


def index(request):
    return render(request, 'home/index.html')


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'home/register.html', {'form': form})
