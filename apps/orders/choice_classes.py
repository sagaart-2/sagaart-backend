from django.db import models


class PaidChoices(models.TextChoices):
    PAID = ('paid', 'Paid')
    NOT_PAID = ('not_paid', 'Not Paid')