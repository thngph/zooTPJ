from django.contrib.auth.models import User
from django.http import HttpResponse
# API- Rest Framework
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .forms import RegistrationForm
from .models import Profile
from .serializers import ProfileSerializer, RegisterSerializer

from animals.models import Animal

# Create your views here.
def index(request):
    data = {'Animals': Animal.objects.all()[:4]}
    user = User.objects.get(id=request.user.id)
    return render(request, 'home/index.html', data, user)


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'home/register.html', {'form': form})


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

