from django.db import models




# Create your models here.
class Libro(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    paginas = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    agregado = models.DateTimeField(auto_now_add=True)
    disponible = models.BooleanField()

    def __str__(self):
        return self.nombre