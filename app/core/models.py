from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.utils.translation import gettext as _


# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email: str, password: str, **extra_fields):
        ''' creates and saves a new user'''
        if not email:
            raise ValueError('Invalid Email!')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str):
        ''' creates and saves a new superuser'''
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''Custom user model that supports using email instead of username'''
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    name = models.CharField(_("Name"), max_length=255)
    is_active = models.BooleanField(_("Is Active?"), default=True)
    is_staff = models.BooleanField(_("Is Staff?"), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
