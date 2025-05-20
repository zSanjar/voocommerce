from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .serializers import CategoryUpdateSerializer
from products.models import Category

class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    lookup_field = "pk"
    
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def put(self, request, *args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
