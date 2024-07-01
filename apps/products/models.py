from django.contrib.auth.hashers import check_password, make_password
from django.core.validators import RegexValidator
from django.db import models

from apps.products import choice_classes


class Artist(models.Model):
    """Модель художника-продавца."""

    name = models.CharField("Имя", max_length=50)
    lastname = models.CharField("Фамилия", max_length=50)
    gender = models.CharField(
        "Пол", max_length=50, choices=choice_classes.GenderChoice.choices
    )
    bio = models.TextField("Биография", blank=True, null=True)
    photo = models.ImageField("Фото", upload_to="artist_images/")
    phone = models.CharField(
        "Телефон",
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Номер телефона должен быть в формате: '+999999999'. Допускается до 15 цифр.",
            )
        ],
    )
    email = models.EmailField("Почта", unique=True)
    date_of_birth = models.DateField("Дата рождения")
    city_of_birth = models.CharField("Город рождения", max_length=100)
    city_of_residence = models.CharField("Город проживания", max_length=100)
    country = models.CharField("Страна рождения", max_length=100)
    education = models.CharField(
        "Образование", max_length=200, null=True, blank=True
    )
    art_education = models.CharField(
        "Художественное образование", max_length=200, null=True, blank=True
    )
    teaching_experience = models.CharField(
        "Опыт преподавания",
        max_length=10,
        choices=choice_classes.YesNoChoices.choices,
    )
    personal_style = models.CharField(
        "Индивидуальный стиль",
        max_length=10,
        choices=choice_classes.YesNoChoices.choices,
    )
    solo_shows = models.ManyToManyField(
        "SoloShow",
        verbose_name="информация о сольных выставках",
        blank=True,
        related_name="artists",
    )
    group_shows = models.ManyToManyField(
        "GroupShow",
        verbose_name="информация о групповых галереях",
        blank=True,
        related_name="artists",
    )
    collected_by_private_collectors = models.BooleanField(
        verbose_name="Коллекционеры которые собирали работы художника",
    )
    collected_by_major_institutions = models.BooleanField(
        verbose_name="Крупные учреждения",
    )
    industry_award = models.TextField(
        verbose_name="Награды", null=True, blank=True
    )
    social = models.URLField(verbose_name="Соц.сети", blank=True, default="")
    create_at = models.DateTimeField("Дата создания", auto_now_add=True)
    password = models.CharField("Пароль", max_length=128)

    def save(self, *args, **kwargs):
        if not self.pk or "password" in kwargs.get("update_fields", []):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    class Meta:
        verbose_name = "художник"
        verbose_name_plural = "художники"
        ordering = ["-date_of_birth"]

    def __str__(self):
        return f"{self.name} {self.lastname}"


class Exhibition(models.Model):
    """Модель выставок."""

    year = models.IntegerField("Год")
    title = models.CharField("Название", max_length=200)
    place = models.CharField("Место", max_length=100)
    city = models.CharField("Город", max_length=100)
    country = models.CharField("Страна", max_length=100)

    class Meta:
        verbose_name = "выставка"
        verbose_name_plural = "выставки"


class SoloShow(Exhibition):
    """Модель сольных выставок."""

    class Meta:
        verbose_name = "сольная выставка"
        verbose_name_plural = "сольные выставки"


class GroupShow(Exhibition):
    """Модель групповых выставок."""

    class Meta:
        verbose_name = "групповая выставка"
        verbose_name_plural = "групповые выставки"


class Style(models.Model):
    """Модель стиля картины."""

    name_style = models.CharField("Название стиля", max_length=50)

    class Meta:
        verbose_name = "стиль"
        verbose_name_plural = "стили"
        ordering = ["-id"]

    def __str__(self):
        return self.name_style


class Category(models.Model):
    """Модель категории."""

    name_category = models.CharField("Название категории", max_length=50)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["-id"]

    def __str__(self):
        return self.name_category


class ProductCard(models.Model):
    """Модель карточки товара."""

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        verbose_name="художник",
        related_name="artworks",
    )
    photo = models.ImageField("Фото", upload_to="product_images/")
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", max_length=200)
    width = models.FloatField(verbose_name="ширина картины")
    heigth = models.FloatField(verbose_name="высота картины")
    genre = models.CharField("Жанр", max_length=100)
    style = models.ForeignKey(
        Style,
        on_delete=models.CASCADE,
        verbose_name="Стиль",
        related_name="product_cards",
    )
    material_work = models.CharField("Материал", max_length=100)
    material_tablet = models.CharField("Материал подложки", max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    year_create = models.IntegerField(verbose_name="Год создания картины")
    avg_cost_of_work = models.DecimalField(
        "Средняя стоимость работы", max_digits=10, decimal_places=2
    )
    price = models.DecimalField(
        "Цена продажи", max_digits=10, decimal_places=2
    )
    desired_price = models.DecimalField(
        "Желаемая цена продажи", max_digits=10, decimal_places=2
    )
    unique = models.BooleanField(verbose_name="уникальность")
    investment_attractiveness = models.BooleanField(
        verbose_name="инвестиционная привелкательность"
    )

    class Meta:
        verbose_name = "карточка товара"
        verbose_name_plural = "карточки товаров"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.artist.name} " f"{self.artist.lastname} - {self.genre}"


# class Bid(models.Model):
#     """Модель заявки."""

#     # Поля из модели Artist
#     artist_name = models.CharField("Имя художника", max_length=50)
#     artist_lastname = models.CharField("Фамилия художника", max_length=50)
#     gender = models.CharField(
#         "Пол", max_length=50, choices=choice_classes.GenderChoice.choices
#     )
#     сity_of_residence = models.CharField("Город проживания", max_length=100)
#     solo_shows = models.ManyToManyField(
#         "SoloShow",
#         verbose_name="информация о сольных выставках",
#         blank=True,
#         related_name="bids",
#     )
#     group_shows = models.ManyToManyField(
#         "GroupShow",
#         verbose_name="информация о групповых галереях",
#         blank=True,
#         related_name="bids",
#     )

#     # Поля из модели ProductCard
#     category = models.ForeignKey(
#         Category, on_delete=models.CASCADE, verbose_name="Категория"
#     )
#     year_create = models.IntegerField(verbose_name="Год создания картины")
#     height = models.FloatField(verbose_name="высота картины")
#     width = models.FloatField(verbose_name="ширина картины")
#     material_work = models.CharField("Материал", max_length=100)
#     material_tablet = models.CharField("Материал подложки", max_length=100)

#     # Дополнительные поля
#     count_title = models.IntegerField("Количество вхождений названия", default=0)
#     count_artist = models.IntegerField("Количество вхождений имени художника", default=0)
#     age = models.IntegerField("Возраст художника", null=True, blank=True)
#     is_alive = models.BooleanField("Живой художник", default=True)

#     def save(self, *args, **kwargs):
#         # Пример логики для расчета возраста художника
#         if self.artist_name and self.artist_lastname:
#             try:
#                 artist = Artist.objects.get(name=self.artist_name, lastname=self.artist_lastname)
#                 self.age = (timezone.now().date() - artist.date_of_birth).days // 365
#             except Artist.DoesNotExist:
#                 self.age = None
#         super().save(*args, **kwargs)


class Bid(models.Model):
    """Модель заявки."""

    product_card = models.ForeignKey(
        ProductCard,
        on_delete=models.CASCADE,
        verbose_name="Карточка товара",
        related_name="bid",
    )
    price = models.DecimalField(
        "Прогнозируемая цена", max_digits=10, decimal_places=2
    )

    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "заявки"
        ordering = ["-id"]

    def __str__(self):
        return f"Цена товара {self.product_card.title} - {self.price}"
