from django.contrib import admin

from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "is_staff", "is_active")
    filter_horizontal = (
        "favorite_style",
        "favorite_category",
        "favorite_artist",
    )
    search_fields = (
        "email",
        "phone",
    )
    ordering = ("email",)
