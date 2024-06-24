from rest_framework import serializers
from .models import Category, Product, ProductImage, CategoryImage, Comment

class CategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = ['category_image_id', 'image', 'alt_text', 'created_at', 'updated_at']

class CategorySerializer(serializers.ModelSerializer):
    images = CategoryImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['category_id', 'name', 'description', 'created_at', 'updated_at', 'images']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product_image_id', 'image', 'alt_text', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_id', 'user_name', 'text', 'created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all(),
        write_only=True,
        source='categories'
    )
    
    class Meta:
        model = Product
        fields = [
            'product_id', 'name', 'price', 'short_description', 
            'created_at', 'updated_at', 'images', 'comments', 
            'categories', 'category_ids'
        ]

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        product = Product.objects.create(**validated_data)
        product.categories.set(categories_data)
        return product

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories', None)
        instance = super().update(instance, validated_data)
        if categories_data:
            instance.categories.set(categories_data)
        return instance
