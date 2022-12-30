from django.contrib import admin
from apps.catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag_thumbnail', 'price', 'quantity']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ['name']}
