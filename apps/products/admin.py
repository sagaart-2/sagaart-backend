from django.contrib import admin

from apps.products.models import Painter, ProductCard


@admin.register(Painter)
class PainterAdmin(admin.ModelAdmin):
    list_display = ("id", "lastname_artist", "date_of_birth")
    search_fields = ("lastname_artist", "date_of_birth")


@admin.register(ProductCard)
class ProductCardAdmin(admin.ModelAdmin):
    list_display = ("artist", "painting_data_create")
    search_fields = ("artist__lastname_artist", "painting_data_create")
