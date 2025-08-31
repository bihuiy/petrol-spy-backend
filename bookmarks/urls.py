from django.urls import path
from .views import BookmarkDetailView, BookmarkListView

urlpatterns = [
    path("", BookmarkListView.as_view()),
    path("<int:pk>/tag/", BookmarkDetailView.as_view()),
]
