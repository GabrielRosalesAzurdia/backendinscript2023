from django.db import models

class Tarjeta1 (models.Model):
    numTelefono = models.CharField(max_length=100)
    numTelefonoEmergencia = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.BooleanField()
    numWhatsapp = models.CharField(max_length=100)