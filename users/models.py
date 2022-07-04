from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.'
                )
        return self.create_user(user_name, first_name, password, **other_fields)

    def create_user(self, user_name, first_name, password, **other_fields):
        if not user_name:
            raise ValueError(_('You must provide an user'))
        
        user = self.model(user_name=user_name, first_name=first_name, **other_fields)

        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    DEPARTAMENTS = (
        (1, 'Omborxona'),
        (2, 'Rahbariyat'),
        (3, 'Mexanika'),
        (4, 'Eksplatatsiya'),
        (5, 'Admin')
    )
    
    #email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    middle_name = models.CharField(max_length=150, blank=True)
    departament = models.CharField(max_length=1, choices=DEPARTAMENTS, blank=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'middle_name', 'departament']

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.user_name