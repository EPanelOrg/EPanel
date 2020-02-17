from rest_framework import serializers
from EPanel.core.models import Device, Home, Section,Profile
from .models import Demand_supply


class DeviceSerializer(serializers.Serializer):
    consuming_power = serializers.IntegerField()
    device_name = serializers.CharField()

    class Meta:
        model = Device
        fields = ("consuming_power", "device_name")


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


class HomeSerializer(serializers.Serializer):
    owner = serializers.CharField()
    active = serializers.BooleanField()
    type = serializers.CharField()
    address = serializers.CharField()
    pk = serializers.IntegerField()

    class Meta:
        model = Home
        fields = ('owner', 'active', 'pk')

class ProfileSerializer(serializers.Serializer):
    email = serializers.EmailField()
    user = serializers.CharField(source='user.pk')
    credit = serializers.IntegerField()
    CitizenshipNo = serializers.IntegerField()
    BDate = serializers.DateField()
    name = serializers.CharField()
    lastName = serializers.CharField()

    class Meta:
        model = Profile
        fields = ('email', 'credit', 'user')


class SectionSerializer(serializers.Serializer):
    home_id = serializers.CharField(source='home.pk')

    class Meta:
        model = Section
        fields = ('home')