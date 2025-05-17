from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from products.models import Color
from .serializers import ColorListSerializer

class ColorListAPIView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

class ColorRetrieveAPIView(RetrieveAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorListSerializer
    lookup_field = "pk"
