from django.apps import apps
import celery

@celery.shared_task()
def process_upload(upload_id: int):
    apps.get_model("app.Upload")._meta.model.objects.filter(id=upload_id).update(processed=True)
