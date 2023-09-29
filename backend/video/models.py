from django.db import models


class VideoRecording(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    # 'videos/' is the folder where videos will be saved
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
