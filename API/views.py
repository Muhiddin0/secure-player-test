import os
from django.http import HttpResponse, StreamingHttpResponse
from .models import Videos
from wsgiref.util import FileWrapper


def stream_video(request, video_id):
    video = Videos.objects.get(id=video_id)
    video_file = video.video

    # Open the video file using a context manager
    video_file = open(video_file.path, 'rb')
    
    try:
        def generate():
            try:
                chunk = video_file.read(1024)  # Adjust chunk size as needed
                while chunk:
                    yield chunk
                    chunk = video_file.read(1024)
            finally:
                video_file.close()

        response = StreamingHttpResponse(generate(), content_type='video/mp4')
        return response
    except FileNotFoundError:
        return HttpResponse("File not found", status=404)