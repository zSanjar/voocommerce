from rest_framework.generics import DestroyAPIView
from products.models import Color

class ColorDeleteAPIView(DestroyAPIView):
    queryset = Color.objects.all()
    lookup_field = "pk"
