from rest_framework import serializers
from .models import Demand_supply

class DS_Serializer(serializers.Serializer):

    homeID = serializers.IntegerField(read_only=True)
    demand = serializers.FloatField(default=0)
    supply = serializers.FloatField(default=0)

    def create(self, validated_data):
        return Demand_supply.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.demand = validated_data.get('demand', instance.demand)
        instance.supply = validated_data.get('supply', instance.supply)
        instance.save()
        return instance
