# app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = False