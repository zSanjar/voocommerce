from rest_framework import serializers
from products.models import Category


class CategoryUpdateSerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]