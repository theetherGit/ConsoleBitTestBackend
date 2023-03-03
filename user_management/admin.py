from django.contrib import admin

from user_management.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'is_active', 'date_joined']
    fields = ['email', 'full_name', 'password']



