import time

from django.test import TestCase, client
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from rest_framework import status

from app.models import Upload


class SimpleTest(TestCase):
    @classmethod
    def create_test_data(cls):
        cls.upload = Upload.objects.first()
        if cls.upload:
            return
        cls.upload = upload = Upload()
        upload.file.save("UploadDemo.txt", ContentFile("Upload Demo 1"))
        upload.save()
    
    def setUp(self) -> None:
        self.create_test_data()
        self.client = client.Client(enforce_csrf_checks=False)
        self.axios = APIClient()
        return super().setUp()
    
    def test_upload_model(self):
        upload = Upload()
        upload.file.save("Upload1.txt", ContentFile("Upload 1"))
        self.assertFalse(upload.processed)
        upload.save()
        time.sleep(2)
        upload.refresh_from_db()
        self.assertIsInstance(upload.pk, int)
        self.assertTrue(upload.processed)

    def test_upload_list_view(self):
        res = self.axios.get("/upload/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertGreater(len(res.data), 0)

    def test_upload_create_view(self):
        uploads_count = Upload.objects.count()
        file = SimpleUploadedFile("file.mp4", b"file_content", content_type="video/mp4")
        sdata = {
            "file": file
        }
        res = self.client.post("/upload/", sdata)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        time.sleep(2)
        self.assertTrue(Upload.objects.last().processed)
        self.assertGreater(Upload.objects.count(), uploads_count)

    def test_upload_detail_view(self):
        res = self.axios.get(f"/upload/{self.upload.pk}/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["id"], self.upload.pk)

    def test_upload_delete_view(self):
        res = self.axios.delete(f"/upload/{self.upload.pk}/")
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.create_test_data()

