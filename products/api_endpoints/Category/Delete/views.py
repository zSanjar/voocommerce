from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from products.models import Category

class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = "pk"
    permission_classes = []

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
