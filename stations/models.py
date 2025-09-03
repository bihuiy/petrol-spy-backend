from django.db import models


# Create your models here.
class Station(models.Model):
    station_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.name} ({self.address})"
