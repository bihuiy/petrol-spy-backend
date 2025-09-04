from django.urls import path
from .views import StationListView, StationDetailView, StationBookmarkView

urlpatterns = [
    path("", StationListView.as_view()),
    path("<int:pk>/", StationDetailView.as_view()),
    path("<str:station_id>/bookmark/", StationBookmarkView.as_view()),
]
