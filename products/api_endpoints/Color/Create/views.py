from rest_framework.generics import CreateAPIView
from products.models import Color
from .serializers import ColorCreateSerializer

class ColorCreateAPIView(CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorCreateSerializer
    permission_classes = []
