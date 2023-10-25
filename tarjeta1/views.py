from django.shortcuts import render
from rest_framework import viewsets
from .models import Tarjeta1
from .serializers import Tarjeta1Serialier

class Tarjeta1View (viewsets.ModelViewSet):
    queryset = Tarjeta1.objects.all()
    serializer_class = Tarjeta1Serialier