from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    profileImage = models.ImageField(upload_to="profile_images/", null=True, blank=True)
