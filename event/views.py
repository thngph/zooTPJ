from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from home.models import Profile
from .models import Event, Comment
from django.views.generic import DetailView
from django.db.models import Q
import unidecode


def remove_accent(text):
    return unidecode.unidecode(text)


# Create your views here.
def index(request):
    event = Event.objects.all().order_by('-date_uploaded')
    page_number = request.GET.get('page')
    paginator = Paginator(event, 8)  # Show 8 posts mỗi page
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # Nếu page_number không thuộc kiểu integer, trả về page đầu tiên
        page = paginator.page(1)
    except EmptyPage:
        # Nếu page không có item nào, trả về page cuối cùng
        page = paginator.page(paginator.num_pages)
    data = {}
    if request.user.is_authenticated:
        data = {'Event': page,
                'Profile': Profile.objects.get(user_ID=request.user.id)}
    else:
        data = {'Event': page}
    # Phantrang
    return render(request, 'event/news.html', data)


def search(request):
    search_str = remove_accent(request.POST['search'])
    result = Event.objects.filter(Q(title_normalized__icontains=search_str) | Q(description_normalized__icontains=search_str))
    if request.user.is_authenticated:
        data = {'Event': result,
                'Profile': Profile.objects.get(user_ID=request.user.id)}
    else:
        data = {'Event': result}
    return render(request, 'event/news.html', data)


def post_main(request, event_id):
    try:
        #     post = {}
        event = Event.objects.get(event_ID=event_id)
        comments = Comment.objects.filter(post_id=event_id)
        if request.user.is_authenticated:
            data = {'post': event,
                    'Profile': Profile.objects.get(user_ID=request.user.id),
                    'Comments': comments
                    }
        else:
            data = {'post': event,
                    'Comments': comments
                    }
        # post = Event.objects.get(event_ID=event_id)
    except Event.DoesNotExit:
        raise Http404("This Post does not exist")
    return render(request, 'event/post.html', data)


@login_required(login_url='login')
def post_comment(request):
    if request.method == 'POST':
        user = Profile.objects.get(user_ID=request.user.id)
        post = Event.objects.get(event_ID=request.POST['post'])
        text = request.POST['text']
        comment = Comment(author=user, post=post, text=text)
        comment.save()
    return HttpResponseRedirect(request.POST['post'])


@login_required(login_url='login')
def delete_comment(request):
    comment = Comment.objects.get(comment_ID=request.POST['comment_id'])
    comment.delete()
    post = Event.objects.get(event_ID=request.POST['post'])
    return HttpResponseRedirect(request.POST['post'])
