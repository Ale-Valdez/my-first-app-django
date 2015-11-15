from django.shortcuts import render
from .models import Pelicula

def peliculas_lista(request):
    peliculas = Pelicula.objects.all().order_by('titulo')
    return render(request, 'movies/peliculas_lista.html', {'peliculas':peliculas})

