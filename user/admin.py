from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'get_full_name', 'email', 'is_active', 'is_superuser')
    list_editable = ('is_active', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_superuser')
