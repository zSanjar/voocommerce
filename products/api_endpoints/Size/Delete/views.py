from rest_framework.generics import DestroyAPIView
from products.models import Size

class SizeDeleteAPIView(DestroyAPIView):
    queryset = Size.objects.all()
    lookup_field = "pk"
