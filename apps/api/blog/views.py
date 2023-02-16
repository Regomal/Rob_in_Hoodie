from rest_framework import permissions, viewsets
from apps.blog.models import Article
from apps.api.blog.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer

    queryset = Article.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'delete']:
            return [permission() for permission in [permissions.IsAdminUser]]
        else:
            return [permission() for permission in [permissions.AllowAny]]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Article.objects.all()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        user = self.request.query_params.get('user')
        if user:
            queryset = queryset.filter(user=user)

        return queryset




