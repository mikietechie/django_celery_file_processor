from django.db.models import Model
import celery

def process_upload(upload: Model):
    upload._meta.model.objects.filter(id=upload.pk).update(processed=True)
