from django.contrib import admin

from apps.products.models import Category, Painter, ProductCard, Style


@admin.register(Painter)
class PainterAdmin(admin.ModelAdmin):
    list_display = ("id", "lastname_artist", "date_of_birth")
    search_fields = ("lastname_artist", "date_of_birth")


@admin.register(ProductCard)
class ProductCardAdmin(admin.ModelAdmin):
    list_display = ("id", "artist", "painting_data_create")
    search_fields = ("artist__lastname_artist", "painting_data_create")


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ("id", "name_style")
    search_fields = ("id", "name_style")


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("id", "name_category")
    search_fields = ("id", "name_category")
