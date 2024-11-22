from django.urls import path

from .views import about, contact

urlpatterns = [
    path('acerca', about, name='about'),
]
