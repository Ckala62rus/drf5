from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


class User(AbstractUser):
    # USERNAME_FIELD = "username"
    # REQUIRED_FIELDS =

    # Временная метка создания объекта.
    created_at = models.DateTimeField(auto_now_add=True)
    # Временная метка показывающая время последнего обновления объекта.
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
