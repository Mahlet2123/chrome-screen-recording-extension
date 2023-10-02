import uuid
import time
from django.http import JsonResponse
from django.views import View
from .models import Video
import os
from django.conf import settings



class CreateVideoView(View):
    def post(self, request):
        # Generate a unique video ID using UUID
        video_id = uuid.uuid4()
        # Create a new Video object with the generated ID
        Video.objects.create(video_id=video_id)
        return JsonResponse({'video_id': str(video_id)})


class AddDataView(View):
    def post(self, request, video_id):
        try:
            video = Video.objects.get(video_id=video_id)
        except Video.DoesNotExist:
            return JsonResponse({'error': 'Video not found'})

        data_chunk = request.body
        video_file_path = os.path.join(settings.MEDIA_ROOT, str(video.video_file))
        with open(video_file_path, 'ab') as video_file:
            video_file.write(data_chunk)

        return JsonResponse({'message': 'Data added successfully'})


class CompleteJobView(View):
    def post(self, request, video_id):
        try:
            video = Video.objects.get(video_id=video_id)
        except Video.DoesNotExist:
            return JsonResponse({'error': 'Video not found'})

        # Mark the video as 'processing' or do any necessary processing here
        video.status = 'processing'
        video.save()

        time.sleep(5)  # Simulate processing time

        video.status = 'complete'
        video.save()
        return JsonResponse({'message': 'Job completed successfully'})

    
class CheckStatusView(View):
    def get(self, request, video_id):
        try:
            video = Video.objects.get(video_id=video_id)
        except Video.DoesNotExist:
            return JsonResponse({'error': 'Video not found'})

        return JsonResponse({'status': video.status})
