from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Roles", {"fields": ("is_admin", "is_user")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Roles", {"fields": ("is_admin", "is_user")}),
    )
