# In your urls.py
from django.urls import path
from .views import stream_video

urlpatterns = [
    path('videos/<int:video_id>/', stream_video, name='stream_video'),
]
