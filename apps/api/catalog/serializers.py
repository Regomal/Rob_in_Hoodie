from rest_framework import serializers
from apps.catalog.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(write_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'descriptions',
            'parent',
            'image',
        )


class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            "slug",
            'descriptions',
            'quantity',
            'price',
        )


class ProductReadSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            "slug",
            'descriptions',
            'quantity',
            'price',
            'categories'
        )

