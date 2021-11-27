from django import forms
import re
from django.contrib.auth.models import User
from home.models import Profile



class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img']
