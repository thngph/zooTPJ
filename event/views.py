from django.shortcuts import render

from home.models import Profile


# Create your views here.


def index(request):
    data = {}
    if request.user.is_authenticated:
        data = {'Profile': Profile.objects.get(user_ID=request.user.id)}
    return render(request, 'event/news.html', data)
