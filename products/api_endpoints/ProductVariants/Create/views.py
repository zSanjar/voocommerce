from rest_framework.generics import CreateAPIView
from products.models import ProductVariant
from .serializers import ProductVariantCreateSerializer

class ProductVariantCreateAPIView(CreateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantCreateSerializer