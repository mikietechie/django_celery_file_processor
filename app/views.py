from django.shortcuts import render, HttpResponse

from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import parsers

from .models import Upload
from .serializers import UploadSerializer

# Create your views here.
def index_view(self):
    return HttpResponse("Hello World, With love St Petersburg, Russia")


class UploadsViewMixin(generics.GenericAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UploadsListView(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        UploadsViewMixin
    ):
    parser_classes = [parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UploadsDetailView(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        UploadsViewMixin
    ):

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
