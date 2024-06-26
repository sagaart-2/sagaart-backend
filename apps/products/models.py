from django.db import models

from apps.products import choice_classes


class Painter(models.Model):
    """Модель художника-продавца."""

    name_artist = models.CharField("Имя", max_length=50)
    lastname_artist = models.CharField("Фамилия", max_length=50)
    gender = models.CharField(
        "Пол", max_length=50, choices=choice_classes.GenderChoice.choices
    )
    date_of_birth = models.DateField("Дата рождения")
    city_of_birth = models.CharField("Город рождения", max_length=100)
    сity_of_residence = models.CharField("Город проживания", max_length=100)
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
    solo_shows = models.TextField(
        "Информация о сольных выставках", null=True, blank=True
    )
    solo_shows_gallery = models.TextField(
        "Сольные галереи", null=True, blank=True
    )
    group_shows = models.TextField(
        "Информация о групповых галереях", null=True, blank=True
    )
    group_shows_gallery = models.TextField(
        "Групповые галереи", null=True, blank=True
    )
    group_shows_artist = models.TextField(
        "Другие художники в групповых галереях", null=True, blank=True
    )
    collected_by_private_collectors = models.TextField(
        verbose_name="Коллекционеры которые собирали работы художника",
        null=True,
        blank=True,
    )
    collected_by_major_institutions = models.TextField(
        verbose_name="Крупные учреждения", null=True, blank=True
    )
    industry_award = models.TextField(
        verbose_name="Награды", null=True, blank=True
    )
    social = models.URLField(verbose_name="Соц.сети", blank=True, default="")

    class Meta:
        verbose_name = "художник"
        verbose_name_plural = "художники"
        ordering = ["-date_of_birth"]

    def __str__(self):
        return f"{self.name_artist} {self.lastname_artist}"


class Style(models.Model):
    """Модель стиля картины."""

    name_style = models.CharField("Название стиля", max_length=50)

    class Meta:
        verbose_name = "стиль"
        verbose_name_plural = "стили"
        ordering = ["-id"]

    def __str__(self):
        return self.name_style


class ProductCard(models.Model):
    """Модель карточки товара."""

    id_card_product = models.AutoField(primary_key=True)
    artist = models.ForeignKey(
        "Painter",
        on_delete=models.CASCADE,
        verbose_name="художник",
        related_name="artworks",
    )
    foto = models.ImageField("Фото", upload_to="product_images/")
    width_painting = models.FloatField(verbose_name="ширина картины")
    heigth_painting = models.FloatField(verbose_name="высота картины")
    type = models.CharField("Тип произведения искусства", max_length=100)
    genre = models.CharField("Жанр", max_length=100)
    style = models.ForeignKey(
        Style,
        on_delete=models.CASCADE,
        verbose_name="Стиль",
        related_name="product_cards",
    )
    material_painting = models.CharField("Материал", max_length=100)
    material_tablet = models.CharField("Материал подложки", max_length=100)
    painting_data_create = models.DateField(
        verbose_name="Год создания картины"
    )
    avg_cost_of_work = models.DecimalField(
        "Средняя стоимость работы", max_digits=10, decimal_places=2
    )
    desired_selling_price = models.DecimalField(
        "Желаемая цена продажи", max_digits=10, decimal_places=2
    )

    class Meta:
        verbose_name = "карточка товара"
        verbose_name_plural = "карточки товаров"
        ordering = ["-id_card_product"]

    def __str__(self):
        return (
            f"{self.artist.name_artist} "
            f"{self.artist.lastname_artist} - {self.type}"
        )


class Category(models.Model):
    """Модель категории."""

    name_category = models.CharField("Название категории", max_length=50)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["-id"]

    def __str__(self):
        return self.name_category
