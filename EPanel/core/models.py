from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Device(models.Model):
    device_name = models.CharField(max_length=30, primary_key=True)
    consuming_power = models.IntegerField()


class Home(models.Model):
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE, default=None)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Section(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, null=False)


class DevicePlan(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, unique=True)
    uptime_per_day = models.IntegerField()
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)

    def get_power_amount(self):
        return self.device.consuming_power * self.uptime_per_day


class Demand_supply(models.Model):
    home_id = models.IntegerField(primary_key=True)
    demand = models.FloatField(default=0, null=True)
    supply = models.FloatField(default=0, null=True)
