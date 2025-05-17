from rest_framework.generics import CreateAPIView
from products.models import Size
from .serializers import SizeCreateSerializer

class SizeCreateAPIView(CreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeCreateSerializer