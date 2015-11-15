from django.db import models


class Dvd(models.Model):
    numero = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return str(self.numero)

class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    nacionalidad = models.CharField(max_length=100, blank=True)
    fecha_nac = models.DateField(null=True)

    def __str__(self):
        return "%s %s" % (self.apellido, self.nombre)

class Genero(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo

class Pelicula(models.Model):
    TIPO_CALIDAD= (
        ('n-n', 'NONE'),
        ('dvd', 'DVD-RIP'),
        ('cam', 'CAM-RIP'),
        ('hd', 'HD'),
    )
    dvd = models.ForeignKey("Dvd")
    titulo = models.CharField(max_length=200)
    anio = models.IntegerField(default=0)
    descripcion = models.TextField()
    calidad = models.CharField(max_length=3, choices=TIPO_CALIDAD, default='n-n')
    duracion = models.TimeField()
    generos = models.ManyToManyField('Genero')
    autores = models.ManyToManyField('Actor')
    vista = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo



	
