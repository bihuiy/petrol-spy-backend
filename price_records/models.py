from django.db import models


# Create your models here.
class PriceRecord(models.Model):
    bookmark = models.ForeignKey(
        to="bookmarks.Bookmark", related_name="price_records", on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        to="users.User", on_delete=models.CASCADE, related_name="owned_price_records"
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    snapshot_price = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.owner} - {self.bookmark} - {self.timestamp}"
