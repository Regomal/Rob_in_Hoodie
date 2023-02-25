from django.contrib import admin
from apps.catalog.models import Category, ProductImage, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


class ProductCategoryInline(admin.TabularInline):
    model = Product.categories.through
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ['image_tag']
    fields = ['product', 'image_tag', 'image', 'is_main']
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    inlines = [ProductCategoryInline, ProductImageInline]
    list_display = ['id', 'image_tag', 'name', 'price', 'quantity', 'user', 'is_checked']
    list_display_links = ['id', 'name', 'image_tag']