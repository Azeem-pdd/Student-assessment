from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import fields, models
from ..models import User
class UserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('email','username')
class UserChangeForm(UserChangeForm):
    class Meta:
        model=User
        fields=('email',)