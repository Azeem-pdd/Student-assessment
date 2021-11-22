from django.contrib.auth.base_user import AbstractBaseUser

from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

from datetime import datetime

from Etesting.settings import USE_I18N

from django.utils import timezone

from django.utils.translation import gettext_lazy as _

# Create your models here.

class MyCustomUserManager(BaseUserManager):
    def create_user(self, email,username, password=None, **extra_fields):
        if not username:
            raise ValueError('There must be a username')
        if not email:
            raise ValueError('There must be an email')
        
        user=self.model(
            email=self.normalize_email(email),
            username=username, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password,**extra_fields):
        
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,
                              username,
                              password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(max_length=50, unique=True)
    email=models.EmailField(verbose_name='email', unique=True)
    identifier=models.CharField(max_length=600, blank=True, null=True)
    first_name=None
    last_name=None
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    
    objects = MyCustomUserManager()
    
    def __str__(self):
        return self.username+','+self.email

    def has_perm(self, perm, obj=None):
        """
        Return True if the user has the specified permission. Query all
        available auth backends, but return immediately if any backend returns
        True. Thus, a user who has permission from a single auth backend is
        assumed to have permission in general. If an object is provided, check
        permissions for that object.
        """
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True
    def has_module_perms(self, app_label):
        """
        Return True if the user has any permissions in the given app label.
        Use similar logic as has_perm(), above.
        """
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True
    
    
    
