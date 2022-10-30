from django.contrib.auth.models import AbstractUser
from django.db import models

from .choices import ROLE_CHOICES
from .managers import UserManager
from .validators import path_and_rename


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=45)
    username = models.CharField(max_length=12, blank=True)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ("-id", )

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    role = models.CharField(max_length=8, choices=ROLE_CHOICES)
    university_name = models.CharField(max_length=2000, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=path_and_rename, blank=True, null=True)

    class Meta:
        ordering = ("-id", )

    def __str__(self):
        return self.user
