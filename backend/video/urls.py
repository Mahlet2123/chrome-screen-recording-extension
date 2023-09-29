from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("api/videos", views.VideoRecordingViewSet, "video-recordings")


urlpatterns = [
    path('', include(router.urls)),
    #path('upload/', views.upload_video, name='upload_video'),
    #path('video/<int:video_id>/', views.view_video, name='view_video'),
]