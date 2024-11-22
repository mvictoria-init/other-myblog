from django.urls import path

from .views import movie, movie_view

urlpatterns = [
    path('', movie, name='movies'),
    path('<str:movie_url>/', movie_view, name='movie_detail'),
]
