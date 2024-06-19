from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, RegexValidator
from django.db import models

from apps.products.models import Painter
from apps.users import choice_classes

PHONE_REGEX = r"^\+7\s?(\d{3})\s?(\d{3})\s?(\d{2})\s?(\d{2})$"


class CustomUser(AbstractUser):
    """Кастомная модель пользователя."""

    username = models.CharField(
        "Username пользователя", max_length=150, unique=False
    )
    phone = models.CharField(
        "Номер телефона",
        max_length=16,
        unique=True,
        help_text="Введите номер телефона",
        validators=[
            RegexValidator(
                regex=PHONE_REGEX,
                message="Номер телефона должен быть в формате '+7 999 999 99 99'.",
                code="invalid_phone_number",
            )
        ],
    )
    email = models.EmailField(
        "Адрес электронной почты",
        max_length=254,
        unique=True,
        help_text="Введите email, не более 254 символа",
        validators=[EmailValidator],
    )
    first_name = models.CharField(
        "Имя", max_length=150, help_text="Введите имя, не более 150 символов"
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=150,
        help_text="Введите фамилию, не более 150 символов",
    )
    surname = models.CharField(
        "Отчество",
        max_length=150,
        help_text="Введите отчество, не более 150 символов",
    )
    # favorite_style = models.ManyToManyField(
    #     Style,
    #     related_name="users_like",
    #     verbose_name="Любимые стили"
    # )
    # favorite_category = models.ManyToManyField(
    #     Category,
    #     related_name="users_like",
    #     verbose_name="Любимые категории"
    # )
    favorite_artist = models.ManyToManyField(
        Painter, related_name="users_like", verbose_name="Любимые художники"
    )
    # subscription = models.ManyToManyField(
    #     Subscription,
    #     related_name="users_like",
    #     verbose_name="Подписки"
    # )
    user_rights = models.CharField(
        "Права пользователя",
        max_length=50,
        choices=choice_classes.UserRightsChoice.choices,
        default="user",
    )
    create_at = models.DateTimeField("Дата cоздания", auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        """Конфигурация кастомной модели пользователя."""

        ordering = ("id",)
        verbose_name = "пользователь"
        verbose_name_plural = "Пользователи"
        constraints = [
            models.UniqueConstraint(
                fields=("phone", "email"), name="unique_phone_email"
            )
        ]

    def __str__(self):
        """Строковое представление объекта пользователя."""
        return self.email

    # @property
    # def is_admin(self):
    #     return self.user_rights == (
    #         choice_classes.UserRightsChoice.ADMIN or self.is_staff
    #     )

    # @property
    # def is_moderator(self):
    #     return self.user_rights == choice_classes.UserRightsChoice.MODERATOR
