from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, username=None, password=None, name=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError("Users must have an email address.")
        if not username:
            username = email
        if not password:
            raise ValueError("Users must have a password.")
        if not name:
            name = username

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password, name):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(
            email=email, username=username, password=password, name=name
        )

        user.is_superuser = True
        user.is_active = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin, TimeStampModel):
    """To Store user basic information"""

    email = models.EmailField(max_length=255, blank=True)
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=30, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "email",
    ]

    def __str__(self):
        return self.username
