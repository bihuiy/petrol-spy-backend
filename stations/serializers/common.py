from rest_framework import serializers
from ..models import Station
from prices.serializers.common import PriceSerializer


class StationSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True, read_only=True)

    class Meta:
        model = Station
        fields = "__all__"
