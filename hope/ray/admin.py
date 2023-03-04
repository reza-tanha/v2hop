from django.contrib import admin
from hope.ray.models import *


@admin.register(ProxyConfig)
class ProxyConfigAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request).prefetch_related("server")
        return queryset
    
    list_display = ("id", "server","volume")
    list_display_links = ("id",)
    empty_value_display = 'UNSET'
    search_fields = ( "conf","server")
    
    
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    
    list_display = ("id", "price","volume")
    list_display_links = ("id",)
    empty_value_display = 'UNSET'
    search_fields = ("price","volume")

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    
    list_display = ("id", "name","username", "password")
    list_display_links = ("id",)
    empty_value_display = 'UNSET'
    search_fields = ("name","username", "password")