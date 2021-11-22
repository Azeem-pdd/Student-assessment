<<<<<<< HEAD
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
=======
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
>>>>>>> 7c053613b36699d9ae280877094b1d43fbe3d2e3
        fields=('email',)