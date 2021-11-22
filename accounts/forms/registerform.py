<<<<<<< HEAD

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
=======

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
>>>>>>> 7c053613b36699d9ae280877094b1d43fbe3d2e3
        fields=( 'username','email',)