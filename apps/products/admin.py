from django.contrib import admin

from apps.products.models import (
    Artist,
    Bid,
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
    filter_horizontal = ("solo_shows", "group_shows")
    search_fields = ("lastname", "date_of_birth")


@admin.register(ProductCard)
class ProductCardAdmin(admin.ModelAdmin):
    list_display = ("id", "artist", "year_create")
    search_fields = ("artist__lastname", "year_create")


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("id", "name")


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("id", "name")


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


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "price")
    readonly_fields = ("price",)
    search_fields = ("title",)
