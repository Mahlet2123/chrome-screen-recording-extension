import uuid
from django.db import models

class Video(models.Model):
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video_file = models.FileField(upload_to='videos/')
    status = models.CharField(max_length=20, default='recording')  # 'recording', 'processing', 'complete'