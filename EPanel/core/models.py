from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Device(models.Model):
    device_name = models.CharField(max_length=30, primary_key=True)
    consuming_power = models.IntegerField()


class Home(models.Model):
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE, default=None)
    power_amount = models.IntegerField(default=0, null=True)
    private_price = models.IntegerField(default=0, null=True)
    type = models.CharField(max_length=10, null=True)


class DevicePlan(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, unique=True)
    uptime_per_day = models.IntegerField()

    def get_power_amount(self):
        return self.device.consuming_power * self.uptime_per_day


class Demand_supply(models.Model):
    home_id = models.IntegerField(primary_key=True)
    demand = models.FloatField(default=0, null=True)
    supply = models.FloatField(default=0, null=True)


class Auction(models.Model):
    auction_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=30)


class Auction_Home(models.Model):
    auction_home_id = models.AutoField(primary_key=True)
    home = models.ForeignKey(Home, null=False, on_delete=models.CASCADE, default=None, related_name='home')
    auction = models.ForeignKey(Auction, null=False, on_delete=models.CASCADE, default=None)
    trade_price = models.IntegerField(default=0)
    traded_with = models.ForeignKey(Home, null=False, on_delete=models.CASCADE, default=None,
                                    related_name='traded_with')
    date_time = models.DateTimeField(default=0, null=True)
    happened = models.IntegerField(default=0)
