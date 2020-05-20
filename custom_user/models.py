from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    displayname = models.CharField(
        max_length=60, default='testing'
    )

    def __str__(self):
        return self.displayname
