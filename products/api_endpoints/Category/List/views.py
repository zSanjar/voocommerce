from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .serializers import CategoryListSerializer
from products.models import Category





class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = []
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        
        return Response(serializer.data)
    
class CategoryRetrieveAPIVIew(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = "pk"
    
    def get(self, request, *args, **kwargs):
        print(request)
        serializer = self.serializer_class(self.get_object())
        
        return Response(serializer.data)
        