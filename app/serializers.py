from rest_framework import serializers
from .models import FractionPrice


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = FractionPrice
        fields = ['fraction', 'price']
