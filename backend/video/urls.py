from django.urls import path
from .views import CreateVideoView, AddDataView, CompleteJobView, CheckStatusView, VideoView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', CreateVideoView.as_view(), name='create_video'),
    path('add_data/<uuid:video_id>/', AddDataView.as_view(), name='add_data'),
    path('complete_job/<uuid:video_id>/', CompleteJobView.as_view(), name='complete_job'),
    path('check_status/<uuid:video_id>/', CheckStatusView.as_view(), name='check_status'),
    path('video/<uuid:video_id>/', VideoView.as_view(), name='view_video')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
