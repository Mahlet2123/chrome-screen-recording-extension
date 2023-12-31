import uuid
import time
from django.http import JsonResponse, FileResponse
from django.views import View
from .models import Video
import os
from django.conf import settings
import base64



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
        if not data_chunk:
            return JsonResponse({'message': 'Invalid Data'})

        video_file_path = os.path.join(settings.MEDIA_ROOT, "videos/sample_video_chunk.bin")

        # Create the video file with the first chunk received
        if not os.path.exists(video_file_path):
            with open(video_file_path, 'wb') as video_file:
                video_file.write(data_chunk)
        else:
            # Append binary data chunks to the video file
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
    
class VideoView(View):
    def get(self, request, video_id):
        try:
            video = Video.objects.get(video_id=video_id)
            video_path = video.video_file.path
        except Video.DoesNotExist:
            return JsonResponse({'error': 'Video not found'})
        
        response = FileResponse(open(video_path, 'rb'), content_type='video/mp4')
        # Adjust the content type as needed
        return response
