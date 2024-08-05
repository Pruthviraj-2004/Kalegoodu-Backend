from django.contrib import admin
from .models import BannerImage, Category, Product, ProductImage, CategoryImage, Comment, SaleType
from import_export.admin import ImportExportModelAdmin

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 1

class ProductAdmin(ImportExportModelAdmin):
    list_display = ('product_id', 'name', 'price', 'discounted_price', 'get_categories', 'get_sale_types', 'created_at', 'updated_at')
    list_filter = ('categories', 'sale_types')
    search_fields = ('name', 'categories__name', 'sale_types__name')
    inlines = [ProductImageInline]

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'

    def get_sale_types(self, obj):
        return ", ".join([sale_type.name for sale_type in obj.sale_types.all()])
    get_sale_types.short_description = 'Sale Types'

admin.site.register(Product, ProductAdmin)

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('category_id', 'name', 'description', 'created_at', 'updated_at')
    inlines = [CategoryImageInline]

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('comment_id', 'product', 'user_name', 'text', 'created_at', 'updated_at')
    list_filter = ('product', 'created_at')
    search_fields = ('user_name', 'product__name')

@admin.register(ProductImage)
class ProductImageAdmin(ImportExportModelAdmin):
    list_display = ('product_image_id', 'product', 'image', 'alt_text', 'created_at', 'updated_at')

@admin.register(CategoryImage)
class CategoryImageAdmin(ImportExportModelAdmin):
    list_display = ('category_image_id', 'category', 'image', 'alt_text', 'created_at', 'updated_at')

@admin.register(SaleType)
class SaleTypeAdmin(ImportExportModelAdmin):
    list_display = ('sale_type_id', 'name')

@admin.register(BannerImage)
class BannerImageAdmin(ImportExportModelAdmin):
    list_display = ('banner_image_id', 'title', 'image', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')