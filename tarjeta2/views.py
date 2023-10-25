from django.shortcuts import render
from rest_framework import viewsets
from .models import Tarjeta2
from .serializers import Tarjeta2Serialier

class Tarjeta2View (viewsets.ModelViewSet):
    queryset = Tarjeta2.objects.all()
    serializer_class = Tarjeta2Serialier