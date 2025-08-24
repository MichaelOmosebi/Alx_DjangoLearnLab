from django.db import models
from django.contrib.auth.models import AbstractUser


# location = models.CharField(max_length=100, blank=True)
# birth_date = models.DateField(null=True, blank=True)
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    followers = models.ManyToManyField('self', related_name='following', symmetrical=False, blank=True)


