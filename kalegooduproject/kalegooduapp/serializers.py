from rest_framework import serializers
from .models import BannerImage, Category, SaleType, Product, ProductImage, CategoryImage, Comment

class SaleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleType
        fields = ['sale_type_id', 'name']

class CategoryImageSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = CategoryImage
        fields = ['category_image_id', 'category', 'category_name', 'image', 'alt_text']

class CategorySerializer(serializers.ModelSerializer):
    images = CategoryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_id', 'name', 'description','images']

class ProductImageSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = ProductImage
        fields = ['product_image_id', 'product', 'product_name', 'image', 'alt_text']

class CommentSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Comment
        fields = ['comment_id', 'product', 'product_name', 'user_name', 'text', 'rating']

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    sale_types = SaleTypeSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_id', 'name', 'price', 'discounted_price', 'video_link', 'short_description', 'categories', 'sale_types', 'images', 'comments']

class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ['banner_image_id', 'title', 'image']