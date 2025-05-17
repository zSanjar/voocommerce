from rest_framework.generics import UpdateAPIView
from products.models import Size
from .serializers import SizeUpdateSerializer

class SizeUpdateAPIView(UpdateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeUpdateSerializer
    lookup_field = "pk"