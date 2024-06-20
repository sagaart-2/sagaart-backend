from django.db import models


class UserRightsChoice(models.TextChoices):
    "Выбор прав пользователя."
    USER = ("user", "Пользователь")
    MODERATOR = ("moderator", "Модератор")
    ADMIN = ("admin", "Администратор")
