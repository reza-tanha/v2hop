from django.urls import path
from .views import *

urlpatterns = [
    path('webhook/', webhook, name="webhook")
]
