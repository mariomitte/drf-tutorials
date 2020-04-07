import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            # User must have email address
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and
        password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='First name of User',
                                 blank=True,
                                 max_length=255)
    last_name = models.CharField(verbose_name='Last name of User',
                                 blank=True,
                                 max_length=255)
    email = models.EmailField(verbose_name='email address',
                              max_length=255,
                              unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(verbose_name='staff status',
                                   default=False,
                                   help_text='Determines if user can access the admin site')
    is_active = models.BooleanField(verbose_name='active',
                                    default=True)
    date_joined = models.DateTimeField(verbose_name='date joined',
                                       default=timezone.now)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
