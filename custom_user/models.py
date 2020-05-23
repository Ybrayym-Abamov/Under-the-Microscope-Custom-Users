from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_super_user(self, email, age, password=None):
        """
        Creates and saves a superuser with the given email, age, and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            age=age
        )
        user.as_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractUser):
    displayname = models.CharField(max_length=60, default='testing')
    age = models.IntegerField(default=0)
    fieldname = models.URLField(max_length=200)

    def __str__(self):
        return self.fieldname
