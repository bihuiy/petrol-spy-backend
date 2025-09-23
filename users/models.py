from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    profileImage = models.URLField(max_length=500, null=True, blank=True)
