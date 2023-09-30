FROM python:3.8

# set a directory for the app
WORKDIR /usr/src/django_celery_file_processor

# copy all the files to the container
COPY . .