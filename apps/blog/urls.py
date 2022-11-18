from django.urls import path
from apps.blog.views import blog_categorie_list

urlpatterns = [
    path('', blog_categorie_list, name='blog_categorie_list'),
]