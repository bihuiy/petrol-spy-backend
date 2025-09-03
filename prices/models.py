from django.db import models


# Create your models here.
class Price(models.Model):
    station = models.ForeignKey(
        to="stations.Station", on_delete=models.CASCADE, related_name="prices"
    )
    fuel_type = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=1)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.station.name} - {self.fuel_type} - {self.price}"
