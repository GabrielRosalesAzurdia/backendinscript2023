from .models import Tarjeta3
from rest_framework import serializers

class Tarjeta3Serialier (serializers.ModelSerializer):
    class Meta:
        model = Tarjeta3
        fields = "__all__"