from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from products.api_endpoints.Category.CategoryCreate.serializers import CategroryCreateSerializer
from products.models import Category


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategroryCreateSerializer
    permission_classes = []
    
    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)