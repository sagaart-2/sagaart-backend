from django.db import models


class GenderChoice(models.TextChoices):
    MALE = ("male", "мужчина")
    FEMALE = ("female", "женщина")
    OTHER = ("other", "другое")


class YesNoChoices(models.TextChoices):
    YES = ("yes", "да")
    NO = ("no", "нет")
