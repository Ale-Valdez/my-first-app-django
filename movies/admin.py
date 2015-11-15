from django.contrib import admin
from .models import Actor
from .models import Pelicula
from .models import Dvd
from .models import Genero

admin.site.register(Actor)
admin.site.register(Pelicula)
admin.site.register(Dvd)
admin.site.register(Genero)
# Register your models here.
