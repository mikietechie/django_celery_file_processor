'''
locust -f stress.py
'''

from locust import FastHttpUser, task
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile


class ApplicationUser(FastHttpUser):
    host = "http://localhost:8000"
    # def on_start(self):
    #     return super().on_start()

    @task()
    def home(self):
        res = self.client.get("/")
        # assert res.status_code == status.HTTP_200_OK

    @task()
    def get_all(self):
        res = self.client.get("/upload/")
        # assert res.status_code == status.HTTP_200_OK

    # @task()
    # def get_one(self):
    #     res = self.client.get(f"/upload/{self.upload.pk}/")
        # assert res.status_code == status.HTTP_200_OK

    # @task()
    # def create(self):
    #     res = self.client.post("/upload/", {
    #         "file": SimpleUploadedFile("file.mp4", b"file_content", content_type="video/mp4")
    #     })
        # assert res.status_code == status.HTTP_201_CREATED