from django.contrib import admin
from .models import Category, Product, ProductImage, CategoryImage, Comment

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'price', 'get_categories', 'created_at', 'updated_at')
    list_filter = ('categories',)
    search_fields = ('name', 'categories__name')
    inlines = [ProductImageInline]

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'

admin.site.register(Product, ProductAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name', 'description', 'created_at', 'updated_at')
    inlines = [CategoryImageInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'product', 'user_name', 'text', 'created_at', 'updated_at')
    list_filter = ('product', 'created_at')
    search_fields = ('user_name', 'product__name')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product_image_id', 'product', 'image', 'alt_text', 'created_at', 'updated_at')

@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):
    list_display = ('category_image_id', 'category', 'image', 'alt_text', 'created_at', 'updated_at')
