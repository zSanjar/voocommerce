from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from common.models import MediaFile
from .serializers import MediaFileListSerializer

class MediaFileListAPIView(ListAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileListSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

class MediaFileRetrieveAPIView(RetrieveAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileListSerializer
    lookup_field = "pk"