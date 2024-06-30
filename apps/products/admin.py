from django.contrib import admin

from apps.products.models import (
    Artist,
    Category,
    Exhibition,
    GroupShow,
    ProductCard,
    SoloShow,
    Style,
)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("id", "lastname", "date_of_birth")
    search_fields = ("lastname", "date_of_birth")


@admin.register(ProductCard)
class ProductCardAdmin(admin.ModelAdmin):
    list_display = ("id", "artist", "year_create")
    search_fields = ("artist__lastname", "year_create")


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ("id", "name_style")
    search_fields = ("id", "name_style")


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("id", "name_category")
    search_fields = ("id", "name_category")


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "place")
    search_fields = ("title", "place")
    list_filter = ("year", "place")


@admin.register(SoloShow)
class SoloShowAdmin(ExhibitionAdmin):
    pass


@admin.register(GroupShow)
class GroupShowAdmin(ExhibitionAdmin):
    pass
