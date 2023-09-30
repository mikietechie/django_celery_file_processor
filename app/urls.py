from django.urls import path

from app.views import UploadsListView, UploadsDetailView, index_view

urlpatterns = [
    path("", index_view),
    path("upload/", UploadsListView.as_view()),
    path("upload/<int:pk>/", UploadsDetailView.as_view()),
]
