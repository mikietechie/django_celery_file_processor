from rest_framework import serializers

from .models import Upload

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = (
            "id",
            "file",
            "uploaded_at",
            "processed"
        )
