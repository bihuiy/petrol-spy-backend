from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bookmark


# Create your views here.
# Path: /bookmarks
class BookmarkListView(APIView):

    # Index route
    def get(self, request):
        bookmarks = Bookmark.objects.all()
