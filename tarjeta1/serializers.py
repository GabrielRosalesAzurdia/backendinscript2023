from .models import Tarjeta1
from rest_framework import serializers

class Tarjeta1Serialier (serializers.ModelSerializer):
    class Meta:
        model = Tarjeta1
        fields = "__all__"