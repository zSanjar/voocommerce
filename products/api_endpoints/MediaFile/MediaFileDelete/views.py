from rest_framework.generics import DestroyAPIView
from common.models import MediaFile

class MediaFileDestroyAPIView(DestroyAPIView):
    queryset = MediaFile.objects.all()
    lookup_field = "pk"