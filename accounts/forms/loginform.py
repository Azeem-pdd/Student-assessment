<<<<<<< HEAD
from django.forms import Form

from django import forms

class LoginForm(Form):
    
    email=forms.EmailField(label='Email', required=True)
    error_css_class = 'error'
    password=forms.CharField(label='Password', max_length=20, required=True,widget=forms.PasswordInput)
=======
from django.forms import Form

from django import forms

class LoginForm(Form):
    
    email=forms.EmailField(label='Email', required=True)
    error_css_class = 'error'
    password=forms.CharField(label='Password', max_length=20, required=True,widget=forms.PasswordInput)
>>>>>>> 7c053613b36699d9ae280877094b1d43fbe3d2e3
    