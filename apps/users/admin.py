from django.contrib import admin

from apps.users.models import CustomUser


@admin.register(CustomUser)
class PainterAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "phone")
    search_fields = ("last_name", "email", "phone")
