from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# API- Rest Framework
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from animals.models import Animal
from donate.models import Donate
from event.models import Event
from ticket.models import Ticket
from .forms import UploadFileForm
from .models import Profile
from .serializers import ProfileSerializer, RegisterSerializer


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        data = {'Animals': Animal.objects.all()[:4],
                'Event': Event.objects.all().order_by('-date_uploaded')[:4],
                'Profile': Profile.objects.get(user_ID=request.user.id),
                'modal': request.GET.get('modal', '')}
    else:
        data = {'Animals': Animal.objects.all()[:4],
                'Event': Event.objects.all().order_by('-date_uploaded')[:4],
                'modal': request.GET.get('modal', '')}
    return render(request, 'home/index.html', data)


def user_info(request):
    profile = None
    if request.user.id:
        profile = Profile.objects.get(user_ID=request.user.id)
    ticket = Ticket.objects.filter(user_ID=request.user.id)
    donate = Donate.objects.filter(user_ID=request.user.id)
    data = {
        'Profile': profile,
        'Ticket': ticket,
        'Donate': donate,
    }
    return render(request, 'home/infoUser.html', data)


@login_required(login_url='login')
def edit_user(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user_ID=request.user.id)
        profile.name = request.POST['name']
        profile.contact = request.POST['contact']
        profile.email = request.POST['email']
        profile.save()
    return redirect('/', {'Profile': profile})


@login_required(login_url='login')
def upload(request):
    if request.method == 'POST':
        # profile.img = request.FILES['img']
        # profile.save()
        profile = Profile.objects.get(user_ID=request.user.id)
        form = UploadFileForm(request.POST, request.FILES, instance=Profile.objects.get(user_ID=request.user.id))
        form.save()
    profile = Profile.objects.get(user_ID=request.user.id)
    return redirect('/', {'Profile': profile})


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        old_pwd = request.POST['old-password']
        pwd_1 = request.POST['password1']
        pwd_2 = request.POST['password2']
        if user.check_password(old_pwd) and pwd_2 == pwd_1:
            user.set_password(pwd_1)
            user.save()
            data = {'Animals': Animal.objects.all()[:4],
                    'Event': Event.objects.all().order_by('-date_uploaded')[:4],
                    'modal': 'welcome'}
            return render(request, 'home/index.html', data)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'home/login.html', {'warning': 'failed'})
    return render(request, 'home/login.html')


def username_exists(username):
    return User.objects.filter(username=username).exists()


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd_1 = request.POST['password1']
        pwd_2 = request.POST['password2']
        email = request.POST['email']
        if username_exists(username):
            return render(request, 'home/register.html', {'warning': 'username'})
        if pwd_1 == pwd_2 and pwd_2:
            user = User.objects.create_user(username, email, pwd_2)
            profile = Profile.objects.create(user_ID=user, email=email)
            profile.save()
            return redirect('/?modal=welcome')

        else:
            return render(request, 'home/register.html', {'warning': 'password'})
    return render(request, 'home/register.html')


# Register API
class RegisterAPI(APIView):
    def get(self, request, *args, **kwargs):
        Obj_User = User.objects.all()
        serializer = RegisterSerializer(Obj_User, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
            # return Response({
            #     # "user": RegisterSerializer(serializer.data),
            #     # "token": AuthToken.objects.create(user)[1],
            # })


# Profile API
class ProfileAPI(APIView):
    def get(self, request, *arg, **kwargs):
        Obj_Profile = Profile.objects.all()
        serializer = ProfileSerializer(Obj_Profile, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # @csrf_exempt
    # def Profile_detail(self, request, pk):
    #     try:
    #         snippet = Profile.objects.get(pk=pk)
    #     except Profile.DoesNotExist():
    #         return HttpResponse(status=404)
    #     Pofile_Detail = Profile.objects.get(pk=pk)
    #     if request.method == 'GET':
    #         serializer = ProfileSerializer(Pofile_Detail)
    #         return Response(serializer.data)
    #
    #     elif request.method == 'PUT':
    #         data = JSONParser().parse(request)
    #         serializer = ProfileSerializer(Pofile_Detail, data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=400)
    #
    #     elif request.method == 'DELETE':
    #         Profile.delete()
    #         return HttpResponse(status=204)
