# app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Blog

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']