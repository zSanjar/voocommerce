from django.contrib import admin

from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone_number", "first_name", "last_name", "is_active", "is_staff")
    list_display_link = ("id", "email", "phone_number", "first_name", "last_name")
    search_fields = ("email", "phone_number", "first_name", "last_name")
    list_filter = ("is_active", "is_staff")