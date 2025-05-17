from rest_framework.generics import UpdateAPIView
from products.models import Color
from .serializers import ColorUpdateSerializer

class ColorUpdateAPIView(UpdateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorUpdateSerializer
    lookup_field = "pk"
