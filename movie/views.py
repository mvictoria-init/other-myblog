from django.shortcuts import render

from .models import Movie

# Create your views here.

def peliculas(resquest):
    movie = Movie.objects.all()
    return render(resquest, 'index.html', {'movie': movie})