from rest_framework import serializers
from EPanel.core.models import Device

class DeviceSerializer(serializers.Serializer):
    consuming_power = serializers.IntegerField()
    device_name = serializers.CharField()
    class Meta:
        model = Device
        fields = ("consuming_power", "device_name")