from django.shortcuts import render
from django.http import Http404
from home.models import Profile
from .models import Event
from django.views.generic import DetailView


# Create your views here.


def index(request):
    data = {}
    if request.user.is_authenticated:
        data = {'Event': Event.objects.all(),
                'Profile': Profile.objects.get(user_ID=request.user.id)}
    else:
        data = {'Event': Event.objects.all()}
    return render(request, 'event/news.html', data)


def post_main(request, event_id):
    try:
        #     post = {}
        if request.user.is_authenticated:
            data = {'post':  Event.objects.get(event_ID=event_id),
                    'Profile': Profile.objects.get(user_ID=request.user.id)}
        else:
            data = { 'post': Event.objects.get(event_ID=event_id)}
        # post = Event.objects.get(event_ID=event_id)
    except Event.DoesNotExit:
        raise Http404("This Post does not exist")
    return render(request, 'event/post.html', data)
