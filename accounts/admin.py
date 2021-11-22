<<<<<<< HEAD
from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.models import User
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms.user_form import UserCreationForm, UserChangeForm
class CustomUserAdmin(UserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm
    model=User
    list_display=('email','is_staff', 'is_active')
    list_filter=('email','is_staff', 'is_active')
    fieldsets=(
        (None,{'fields':('email','password','identifier')},),
    ('permissions',{'fields':('is_staff', 'is_active')},
               ),
        )
    add_fieldsets=((None,
                   {'classes':('wide',),
                   'fields':('email','password1','password2', 'is_staff', 'is_active')},
    
               ),)
    search_fields=('email','username')
    ordering=('email',)
#admin.site.unregister(User)
=======
from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.models import User
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms.user_form import UserCreationForm, UserChangeForm
class CustomUserAdmin(UserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm
    model=User
    list_display=('email','is_staff', 'is_active')
    list_filter=('email','is_staff', 'is_active')
    fieldsets=(
        (None,{'fields':('email','password','identifier')},),
    ('permissions',{'fields':('is_staff', 'is_active')},
               ),
        )
    add_fieldsets=((None,
                   {'classes':('wide',),
                   'fields':('email','password1','password2', 'is_staff', 'is_active')},
    
               ),)
    search_fields=('email','username')
    ordering=('email',)
#admin.site.unregister(User)
>>>>>>> 7c053613b36699d9ae280877094b1d43fbe3d2e3
admin.site.register(User,CustomUserAdmin)