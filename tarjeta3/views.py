from django.shortcuts import render
from rest_framework import viewsets
from .models import Tarjeta3
from .serializers import Tarjeta3Serialier

class Tarjeta3View (viewsets.ModelViewSet):
    queryset = Tarjeta3.objects.all()
    serializer_class = Tarjeta3Serialier