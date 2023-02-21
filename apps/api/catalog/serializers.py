from rest_framework import serializers
from apps.catalog.models import Category, Product, ProductImage


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


class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'id',
            'image',
            'product',
            'is_main'
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
    images = ProductImageSerializers(many=True)
    main_image = ProductImageSerializers

    class Meta:
        model = Product
        fields = (
            'id',
            'images',
            'main_image',
            'name',
            "slug",
            'descriptions',
            'quantity',
            'price',
            'categories'
        )

