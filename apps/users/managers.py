from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """Менеджер пользовательской модели пользователя."""

    def create_user(self, email, password, **extra_fields):
        """Создать пользователя с паролем и электронной почтой."""
        if not email:
            raise ValueError("Введите email")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Создать суперпользователя с паролем и электронной почтой."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Суперпользователь должен иметь is_superuser=True."
            )
        return self.create_user(email, password, **extra_fields)
