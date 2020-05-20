from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    displayname = models.CharField(max_length=60, default='testing')
    age = models.IntegerField(default=0)
    fieldname = models.URLField(max_length=200)

    def __str__(self):
        return self.fieldname
