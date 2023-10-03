# sudo docker build -t mikietechie/django_celery_file_processor .
# sudo docker run -p 8000:8000 mikietechie/django_celery_file_processor
# sudo docker run -t -p 8000:8000 mikietechie/django_celery_file_processor bash
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y  curl git redis-server python3 python3-pip python3-venv
# git clone https://github.com/mikietechie/django_celery_file_processor
copy . django_celery_file_processor

WORKDIR /django_celery_file_processor

# Environment Variables
ENV CELERY_BROKER_URL = redis://localhost:6379
ENV CELERY_RESULT_BACKEND = redis://localhost:6379

EXPOSE 8000
# RUN python3 -m venv env
# CMD env/bin/activate
RUN pip3 install -r requirements.txt
CMD ["ls"]
CMD python3 manage.py runserver 8000