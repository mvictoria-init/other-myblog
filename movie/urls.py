from django.urls import path

from .views import peliculas

urlpatterns = [
    path('', peliculas, name='movies'),
]
