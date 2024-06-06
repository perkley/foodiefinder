from django.urls import path
from .views import favorites

app_name = 'favorites'

urlpatterns = [
    path('', favorites, name='favorites'),
]