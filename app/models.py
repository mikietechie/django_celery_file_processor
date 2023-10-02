from django.db import models
from django.core.exceptions import ValidationError

from .tasks import process_upload


class Upload(models.Model):
    '''
    Simple Model for managing uploads and coordinating their processing
    '''

    file = models.FileField(upload_to="uploads")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        str_pk = str(self.pk)
        justify = '0' * (8-len(str_pk))
        return f"UPLOAD-{justify}{str_pk}"
    
    def validate_already_processed(self):
        if self.pk and self.processed:
            raise ValidationError("You cannot alter a processed upload")
        
    def trigger_file_processor(self):
        process_upload.delay(self.pk)
    
    def save(self, *args, **kwargs) -> None:
        self.validate_already_processed()
        super().save(*args, **kwargs)
        if not self.processed:
            self.trigger_file_processor()
