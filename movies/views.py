from django.shortcuts import render

def peliculas_lista(request):
    return render(request, 'movies/peliculas_lista.html', {})
# Create your views here.
