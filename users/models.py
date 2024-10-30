from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=20, unique=True, verbose_name="Номер телефона")
    email = models.EmailField(
        unique=True, verbose_name="Электронная почта", help_text="Укажите почту"
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
