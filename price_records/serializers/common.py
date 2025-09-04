from rest_framework import serializers
from ..models import PriceRecord
from bookmarks.serializers.common import BookmarkSerializer
from bookmarks.models import Bookmark


class PriceRecordSerializer(serializers.ModelSerializer):
    bookmark = serializers.PrimaryKeyRelatedField(queryset=Bookmark.objects.all())
    bookmark_detail = BookmarkSerializer(source="bookmark", read_only=True)

    class Meta:
        model = PriceRecord
        fields = "__all__"
