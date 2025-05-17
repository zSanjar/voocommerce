from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from products.models import Size
from .serializers import SizeListSerializer

class SizeListAPIView(ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeListSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

class SizeRetrieveAPIView(RetrieveAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeListSerializer
    lookup_field = "pk"
