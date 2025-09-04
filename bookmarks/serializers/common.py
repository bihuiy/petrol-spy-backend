from rest_framework import serializers
from ..models import Bookmark
from stations.serializers.common import StationSerializer


class BookmarkSerializer(serializers.ModelSerializer):
    bookmarked_station = StationSerializer(read_only=True)

    class Meta:
        model = Bookmark
        fields = "__all__"
