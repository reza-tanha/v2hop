from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin




@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request).select_related("factory")
    #     return queryset
    
    list_display = ("id", "username", "user_id", "step")
    list_filter = ("username", "user_id")

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

    search_fields = ('email', 'first_name',"username", "time_zone", "is_admin", "is_verify_operator", "factory__name")
    ordering = ('id', 'email')
    list_filter
    
    
admin.site.register(Balance)