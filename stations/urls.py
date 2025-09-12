from django.urls import path
from .views import StationListView, StationBookmarkView

urlpatterns = [
    path("", StationListView.as_view()),
    path("<str:station_id>/bookmark/", StationBookmarkView.as_view()),
]
