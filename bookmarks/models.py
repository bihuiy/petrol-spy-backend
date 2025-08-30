from django.db import models


# Create your models here.
class Bookmark(models.Model):
    owner = models.ForeignKey(
        to="users.User",
        on_delete=models.CASCADE,
        related_name="owned_bookmarks",
    )

    station = models.ForeignKey(to="stations.Station", on_delete=models.CASCADE)

    tag = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.owner}'s bookmark"
