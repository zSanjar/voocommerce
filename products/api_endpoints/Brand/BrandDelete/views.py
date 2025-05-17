from rest_framework.generics import DestroyAPIView
from products.models import Brand

class BrandDeleteAPIView(DestroyAPIView):
    queryset = Brand.objects.all()
    lookup_field = "pk"
