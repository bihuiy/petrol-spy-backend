from django.urls import path
from .views import StationListView, StationDetailView

urlpatterns = [
    path("", StationListView.as_view()),
    path("<int:pk>/", StationDetailView.as_view()),
]
