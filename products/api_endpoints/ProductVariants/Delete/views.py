from rest_framework.generics import DestroyAPIView
from products.models import ProductVariant

class ProductVariantDeleteAPIView(DestroyAPIView):
    queryset = ProductVariant.objects.all()
    lookup_field = "pk"
