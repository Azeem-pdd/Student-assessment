
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms
from ..models import User
from django.contrib.auth.forms import UserCreationForm

User=get_user_model()
class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=( 'username','email',)