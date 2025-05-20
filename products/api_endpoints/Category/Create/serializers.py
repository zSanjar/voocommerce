from rest_framework import serializers
from products.models import Category

class CategroryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name", "slug"]