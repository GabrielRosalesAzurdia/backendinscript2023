from django.db import models

class Tarjeta2 (models.Model):
    nombreMocoso = models.TextField()
    anosMocoso = models.IntegerField()
    encargado = models.TextField()
    nacimientoMocoso = models.DateField()
    gradoMocoso = models.TextField()
    direccionMocoso = models.TextField()