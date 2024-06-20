from django.contrib import admin

from apps.users.models import CustomUser


@admin.register(CustomUser)
class PainterAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "is_staff", "is_active")
    search_fields = (
        "email",
        "phone",
    )
    ordering = ("email",)
