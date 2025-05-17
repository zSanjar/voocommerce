from rest_framework.generics import DestroyAPIView
from common.models import MediaFile

class MediaFileDeleteAPIView(DestroyAPIView):
    queryset = MediaFile.objects.all()
    lookup_field = "pk"