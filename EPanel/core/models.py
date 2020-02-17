from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Device(models.Model):
    device_name = models.CharField(max_length=30, primary_key=True)
    consuming_power = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.IntegerField()
    email = models.EmailField(default=None, null=True)
    CitizenshipNo = models.IntegerField(null=True)
    BDate = models.DateField(null=True)
    name = models.CharField(max_length = 30,null=True)
    lastName = models.CharField(max_length = 30,null=True)


class Home(models.Model):
    home_id = models.AutoField(primary_key=True, default=0)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE, default=None)
    power_amount = models.IntegerField(default=0, null=True)
    private_price = models.IntegerField(default=0, null=True)
    type = models.CharField(max_length=10, null=True)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE, default=None)
    active = models.BooleanField(default=True)
    type = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.name

    def get_home_daily_usage(self):
        sections = Section.objects.filter(home=self)
        home_daily_usage = 0
        for section in sections:
            home_daily_usage += section.get_section_daily_usage()
        return home_daily_usage

class Section(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, null=False)

    def get_section_daily_usage(self):
        section_DP_list = DevicePlan.objects.filter(section=self)
        section_usage = 0
        for DP in section_DP_list:
            section_usage += DP.get_power_amount()

        return section_usage


class DevicePlan(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    uptime_per_day = models.IntegerField()
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)

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
    home = models.ForeignKey(Home, null=False, related_name="home_in_auction", on_delete=models.CASCADE, default=0)
    auction = models.ForeignKey(Auction, null=False, on_delete=models.CASCADE, default=None)
    trade_price = models.IntegerField(default=0)
    traded_with = models.ForeignKey(Home, null=False, related_name="home_traded_with", on_delete=models.CASCADE,
                                    default=0)
    date_time = models.DateTimeField(default=0, null=True)
    happened = models.IntegerField(default=0)
