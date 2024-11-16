from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(max_length=15, blank=True, null=True, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_stuff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)