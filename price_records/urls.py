from django.urls import path
from .views import PriceRecordDetailView, PriceRecordListView

urlpatterns = [
    path("", PriceRecordListView.as_view()),
    path("<int:pk>/", PriceRecordDetailView.as_view()),
]
