import os
import uuid

from PIL import Image
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


def user_directory_path(instance, filename, ):
    path = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(full_path):
        os.remove(full_path)
    return path


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse()
