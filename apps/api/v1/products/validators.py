from datetime import datetime

from rest_framework import serializers


def validate_date_of_birth(value):
    """Валидация значения поля Дня Рождения."""
    if value > datetime.now().date():
        raise serializers.ValidationError(
            "Дата рождения не может быть больше текущей даты."
        )
    return value


def validate_year_create(value):
    """Валидация значения поля года создания."""
    current_year = datetime.now().year
    if value > current_year:
        raise serializers.ValidationError(
            "Год создания не может быть больше текущего года."
        )
    return value


def validate_price(value):
    """Валидация значения поля цены."""
    if value <= 0:
        raise serializers.ValidationError("Цена должна быть больше 0.")


def validate_width(value):
    """Валидация значения поля ширины картины."""
    if value <= 0:
        raise serializers.ValidationError(
            "Ширина картины должна быть больше 0."
        )


def validate_heigth(value):
    """Валидация значения поля высоты картины."""
    if value <= 0:
        raise serializers.ValidationError(
            "Высота картины должна быть больше 0."
        )


def validate_age(value):
    """Валидация значения поля возраста."""
    if value <= 0:
        raise serializers.ValidationError("Возраст должен быть больше 0.")
