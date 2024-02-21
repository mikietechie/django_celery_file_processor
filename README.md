# Django, DRF Celery File Processor API
An interview assignment.

## Techstack
1. Linux
2. Python
3. Django
4. Django Rest Framework
5. Redis
6. Docker
7. Celery
8. Git

## Instructions
Test task: Uploading and processing files
Goal:
Develop a Django REST API that allows you to upload files to the server and then asynchronously process them using Celery.
Requirements:
Create a Django project and application.
Use Django REST Framework to create an API.
Implement a File model that will represent uploaded files. The model must contain the fields:
file: a field of the FileField type used to upload the file.
uploaded_at: a DateTimeField field containing the date and time the file was uploaded.
processed: a BooleanField field indicating whether the file has been processed.
Implement a serializer for the File model.
Create an upload/endpoint API that will accept POST requests to upload files. When uploading a file, you need to create a File model object, save the file on the server, and run an asynchronous task to process the file using Celery. In response to a successful file upload, return the 201 status and serialized file data.
Implement a Celery task to process the file. The task must be started asynchronously and change the processed field of the File model to True after processing the file.
Implement the files/ endpoint API, which will return a list of all files with their data, including the processing status.
Additional requirements:
Use Docker to deploy the project.
Implement a mechanism for processing various types of files (for example, images, text files, etc.).
Provide error handling and return of appropriate status codes and error messages.
Notes:
When performing the task, it is recommended to use the official documentation of Django, DRF, Celery and Docker.
You can use any additional libraries if you see fit.
Complications:
Tests (try to achieve coverage of 70% or more)
Describe how the architecture will change if we expect a heavy load
Try to estimate how much load your service can withstand in RPS
