from rest_framework.generics import UpdateAPIView
from products.models import Brand
from .serializers import BrandUpdateSerializer

class BrandUpdateAPIView(UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandUpdateSerializer
    lookup_field = "pk"
