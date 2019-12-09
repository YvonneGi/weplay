from django import forms
from .models import *
class ProfileForm(forms.ModelForm):
    class Meta:
         model= Profile
         exclude = ['username','team']
class TeamForm (forms.ModelForm):
    class Meta:
         model = Team

         exclude = ['ground']
# class NewPostForm(forms.ModelForm):
#     class Meta:
#         model = Events
#         exclude = ['posted_by','poster']

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['posted_by','poster','bloger','profile']

class ChatForm (forms.ModelForm):
    class Meta:
        model = Chat
        exclude = ['username','team']


class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['username',' poster']
     
