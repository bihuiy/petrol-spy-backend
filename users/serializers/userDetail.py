from rest_framework import serializers
from ..models import User
from bookmarks.serializers.common import BookmarkSerializer


class UserDetailSerializer(serializers.ModelSerializer):
    owned_bookmarks = BookmarkSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "owned_bookmarks"]
