from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from authentication.managers import UserManager


class User(AbstractBaseUser):

    username = models.CharField(max_length=225, help_text='Your username')
    email = models.EmailField(unique=True, help_text='Your email')
    is_verify = models.BooleanField(default=False, verbose_name='account verified')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["id"]