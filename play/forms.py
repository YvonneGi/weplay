from django import forms
from .models import *
class ProfileForm(forms.ModelForm):
    class Meta:
         model= Profile
         exclude = ['user','team']
class TeamForm (forms.ModelForm):
    class Meta:
         model = Team

         exclude = ['ground']
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Events
        exclude = ['posted_by','poster']


class ChatForm (forms.ModelForm):
    class Meta:
         model = Chat

         exclude = ['username','team']
     
