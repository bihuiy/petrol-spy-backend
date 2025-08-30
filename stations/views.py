from rest_framework.views import APIView
from .models import Station
from rest_framework.response import Response
from .serializers.common import StationSerializer
from rest_framework.exceptions import NotFound


# Create your views here.
# Path: /stations
class StationListView(APIView):

    # Index route
    def get(self, request):
        stations = Station.objects.all()
        serialized_stations = StationSerializer(stations, many=True)
        return Response(serialized_stations.data)


# Path: /stations/<int:pk>
class StationDetailView(APIView):

    # Show route
    def get(self, request, pk):
        try:
            station = Station.objects.get(pk=pk)
            serialized_station = StationSerializer(station)
            return Response(serialized_station.data)
        except Station.DoesNotExist as e:
            raise NotFound("Station does not exist.")
