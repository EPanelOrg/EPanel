from django.db import models

# Create your models here.


class Demand_supply(models.Model):

    home_id = models.IntegerField(primary_key=True)
    demand = models.FloatField(default=0, null=True)
    supply = models.FloatField(default=0, null=True)
