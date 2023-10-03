FROM python:3.11

# set a directory for the app
WORKDIR /usr/src/django_celery_file_processor

# copy all the files to the container
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
#  docker run -p 8000:8000 mikietechie/django_celery_file_processor
CMD ["python", "manage.py", "runserver"]