from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import VideoRecording
from .serializers import VideoRecordingSerializer

class VideoRecordingViewSet(viewsets.ModelViewSet):
    queryset = VideoRecording.objects.all()
    serializer_class = VideoRecordingSerializer


"""@api_view(['POST'])
def upload_video(request):
    serializer = VideoRecordingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Video uploaded successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_video(request, video_id):
    try:
        video = VideoRecording.objects.get(pk=video_id)
        serializer = VideoRecordingSerializer(video)
        return Response(serializer.data)
    except VideoRecording.DoesNotExist:
        return Response({'error': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)
"""