from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin




@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("id", "username", "user_id", "step")
    list_filter = ("username", "user_id", "is_send_ads", "send_ads_time")
    fieldsets = (
        (None, {
            'fields': ('user_id', 'password')
        }),
        ('Personal info', {
            'fields': (
                'first_name',
                'last_name',)
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff',
                'is_superuser', 
                'groups', 'user_permissions')
        })
    )
    search_fields = ('email', 'first_name',"username", "user_id", "is_admin")
    ordering = ('id',)

admin.site.register(Balance)