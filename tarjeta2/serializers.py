from .models import Tarjeta2
from rest_framework import serializers

class Tarjeta2Serialier (serializers.ModelSerializer):
    class Meta:
        model = Tarjeta2
        fields = "__all__"