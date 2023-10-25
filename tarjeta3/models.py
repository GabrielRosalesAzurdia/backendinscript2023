from django.db import models

class Tarjeta3 (models.Model):
    ingresos = models.IntegerField()
    aportafamilia = models.TextField()
    oficioEncargado = models.TextField()