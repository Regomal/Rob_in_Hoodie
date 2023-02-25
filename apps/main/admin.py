from django.contrib import admin
from apps.main.models import Page, ProductSet
from adminsortable2.admin import SortableAdminMixin


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass


class SetProductInline(admin.TabularInline):
    model = ProductSet.products.through
    extra = 1


@admin.register(ProductSet)
class ProductSetAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ["name", "sort", "is_active"]
    inlines = [SetProductInline]



