from rest_framework.views import APIView
from .models import Station
from rest_framework.response import Response
from .serializers.common import StationSerializer
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from bookmarks.models import Bookmark
from bookmarks.serializers.common import BookmarkSerializer


# Create your views here.
# Path: /stations/
class StationListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Index route - display stations on the map as the map center changes
    def get(self, request):
        # Get the bounding params
        bbox = request.query_params.get("bbox", None)
        if bbox:
            left, bottom, right, top = map(
                float, bbox.split(",")
            )  # Use split(",") to convert string to list
            stations = Station.objects.filter(
                longitude__gte=left,
                longitude__lte=right,
                latitude__gte=bottom,
                latitude__lte=top,
            ).prefetch_related("prices")
        else:
            stations = Station.objects.all().prefetch_related("prices")

        serialized_stations = StationSerializer(stations, many=True)
        return Response(serialized_stations.data)


class GetStation:
    # Helper function that gets the object or sends a 404
    def get_station(self, pk):
        try:
            return Station.objects.get(pk=pk)
        except Station.DoesNotExist as e:
            raise NotFound("Station does not exist.")


# Path: /stations/<int:pk>/
class StationDetailView(APIView, GetStation):
    permission_classes = [IsAuthenticated]

    # Show route - display a specific station's details
    def get(self, request, pk):
        station = self.get_station(pk)
        serialized_station = StationSerializer(station)
        return Response(serialized_station.data)


# Path: /stations/<int:pk>/bookmark/
class StationBookmarkView(APIView, GetStation):
    permission_classes = [IsAuthenticated]

    # Create route - add a station to user's bookmark
    def post(self, request, pk):
        station = self.get_station(pk)
        user = request.user
        if Bookmark.objects.filter(owner=user, bookmarked_station=station).exists():
            return Response({"details": "This station is already bookmarked."})

        bookmark = Bookmark.objects.create(owner=user, bookmarked_station=station)
        serialized_bookmark = BookmarkSerializer(bookmark)
        return Response(serialized_bookmark.data, 201)

    # Delete route - remove a station from user's bookmark
    def delete(self, request, pk):
        station = self.get_station(pk)
        user = request.user
        try:
            bookmark = Bookmark.objects.get(owner=user, bookmarked_station=station)
            bookmark.delete()
            return Response(status=204)
        except Bookmark.DoesNotExist as e:
            raise NotFound("Bookmark does not exist.")
