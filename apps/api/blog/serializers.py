from rest_framework import serializers
from apps.blog.models import Article, BlogCategory, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ('id', 'name', 'image')


class ArticleWriteSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(max_length=64), write_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'category',
            'user',
            'image',
            'text',
            'text_preview',
            "tags"
        )


class ArticleReadSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'category',
            'user',
            'image',
            # 'image_thumbnail',
            'text',
            'text_preview',
            'created_at',
            'tags',
        )
