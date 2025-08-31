from django.db import models


# Create your models here.
class PriceRecord(models.Model):
    record_station = models.ForeignKey(
        to="bookmarks.Bookmark", related_name="price_records", on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        to="users.User", on_delete=models.CASCADE, related_name="owned_price_records"
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    snapshot_price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.owner} - {self.record_station} - {self.timestamp}"
