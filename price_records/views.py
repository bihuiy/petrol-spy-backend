from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import PriceRecord
from .serializers.common import PriceRecordSerializer
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, NotFound


# Create your views here.
# Path: /price-records/
class PriceRecordListView(APIView):
    permission_classes = [IsAuthenticated]

    # Index route - display all price records created by this user
    def get(self, request):
        user = request.user
        price_records = PriceRecord.objects.filter(owner=user)
        serialized_price_records = PriceRecordSerializer(price_records, many=True)
        return Response(serialized_price_records.data)

    # Create route - add a realtime price to price record page
    def post(self, request):
        serialized_price_record = PriceRecordSerializer(data=request.data)
        serialized_price_record.is_valid(raise_exception=True)
        serialized_price_record.save()
        return Response(serialized_price_record, 201)


# Path: /price-records/<int:pk>/
class PriceRecordDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # Delete route - remove a price record from the record page
    def delete(self, request, pk):
        try:
            price_record = PriceRecord.objects.get(pk=pk)

            if price_record.owner != request.user:
                raise PermissionDenied(
                    "You don't have the permission to access this resource."
                )

            price_record.delete()
            return Response(status=204)
        except PriceRecord.DoesNotExist as e:
            raise NotFound("Price record does not exist.")
