from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bookmark
from rest_framework.permissions import IsAuthenticated
from .serializers.common import BookmarkSerializer
from rest_framework.exceptions import NotFound, PermissionDenied


# Create your views here.
# Path: /bookmarks/
class BookmarkListView(APIView):
    permission_classes = [IsAuthenticated]

    # Index route - display all bookmarked stations by this user
    def get(self, request):
        user = request.user
        bookmarks = Bookmark.objects.filter(owner=user)
        serialized_bookmarks = BookmarkSerializer(bookmarks, many=True)
        return Response(serialized_bookmarks.data)


# Path: /bookmarks/<int:pk>/tag/
class BookmarkDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # Helper function that gets the object or sends a 404
    def get_bookmark(self, pk):
        try:
            return Bookmark.objects.get(pk=pk)
        except Bookmark.DoesNotExist as e:
            raise NotFound("Bookmark does not exist.")

    # Update route - add/update a tag for a bookmarked station
    def put(self, request, pk):
        bookmark = self.get_bookmark(pk)
        serialized_bookmark = BookmarkSerializer(
            bookmark, data=request.data, partial=True
        )
        serialized_bookmark.is_valid(raise_exception=True)
        serialized_bookmark.save()
        return Response(serialized_bookmark.data)

    # Delete route - delete a tag for a bookmarked station
    def delete(self, request, pk):
        bookmark = self.get_bookmark(pk)

        if bookmark.owner != request.user:
            raise PermissionDenied(
                "You don't have the permission to access this resource."
            )

        bookmark.tag = None
        bookmark.save()
        return Response(status=204)
