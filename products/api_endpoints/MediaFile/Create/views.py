# MediaFileCreate/views.py
from rest_framework.generics import CreateAPIView
from common.models import MediaFile
from .serializers import MediaFileCreateSerializer

class MediaFileCreateAPIView(CreateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileCreateSerializer
