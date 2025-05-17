from rest_framework.generics import ListAPIView, RetrieveAPIView
from products.models import Brand
from .serializers import BrandListSerializer
from rest_framework.response import Response

class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

class BrandRetrieveAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    lookup_field = "pk"
