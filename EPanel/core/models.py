from django.db import models


# Create your models here.
class Device(models.Model):
    device_name = models.CharField(max_length=30, primary_key=True)
    consuming_power = models.IntegerField()



class DevicePlan(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, unique=True)
    uptime_per_day = models.IntegerField()

    def get_power_amount(self):
        return self.device.consuming_power * self.uptime_per_day
