from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from home.models import Profile
from .models import Event, Comment
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
            event = Event.objects.get(event_ID=event_id)
            comments = Comment.objects.filter(author_id=request.user.id).filter(post_id=event_id)
            data = {'post': event,
                    'Profile': Profile.objects.get(user_ID=request.user.id),
                    'Comments': comments
                    }
        else:
            data = {'post': Event.objects.get(event_ID=event_id)}
        # post = Event.objects.get(event_ID=event_id)
    except Event.DoesNotExit:
        raise Http404("This Post does not exist")
    return render(request, 'event/post.html', data)


@login_required
def post_comment(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        post = Event.objects.get(event_ID=request.POST['post'])
        text = request.POST['text']
        comment = Comment(author=user, post=post, text=text)
        comment.save()
    return HttpResponseRedirect(request.POST['post'])
