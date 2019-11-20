from django import forms
from .models import *
class ProfileForm(forms.ModelForm):
     class Meta:
         model= Profile
         exclude = ['user','team']
class TeamForm (forms.ModelForm):
     class Meta:
         model = Team
         exclude = ['']