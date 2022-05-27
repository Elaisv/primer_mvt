from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=35)
    edad = models.IntegerField()
    fecha_nac = models.DateTimeField()

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nacimiento: {self.fecha_nac}"