from rest_framework import serializers
from products.models import ProductVariant

class ProductVariantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ["id", "name", "price", "product", "images", "stock", "color", "size", "is_active"]