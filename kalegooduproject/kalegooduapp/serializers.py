from rest_framework import serializers
from .models import BannerImage, Category, Customer, Order, OrderItem, PageContent, PageImage, SaleType, Product, ProductImage, CategoryImage, Comment, Workshop, WorkshopImage, WorkshopVideo

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
        fields = ['comment_id', 'product', 'product_name', 'user_name', 'text', 'rating','display']

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    sale_types = SaleTypeSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_id', 'name', 'price', 'quantity','discounted_price', 'video_link', 'short_description', 'categories', 'sale_types', 'images', 'comments']

class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ['banner_image_id', 'title', 'image']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['order_item_id', 'order', 'product', 'product_name', 'quantity', 'price', 'order_completed']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    customer_name = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = Order
        fields = ['order_id', 'customer', 'customer_name', 'total_amount', 'count', 'order_completed', 'created_at', 'updated_at', 'items']

class PageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageImage
        fields = ['pageimage_id', 'image', 'created_at', 'updated_at']

class PageContentSerializer(serializers.ModelSerializer):
    images = PageImageSerializer(many=True, read_only=True)

    class Meta:
        model = PageContent
        fields = ['pagecontent_id', 'page_name', 'content', 'created_at', 'updated_at', 'images']

class WorkshopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopImage
        fields = ['workshopimage_id', 'image']

class WorkshopVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopVideo
        fields = ['workshopvideo_id', 'video_url']

# class WorkshopSerializer(serializers.ModelSerializer):
#     images = WorkshopImageSerializer(many=True, read_only=True)
#     videos = WorkshopVideoSerializer(many=True, read_only=True)

#     class Meta:
#         model = Workshop
#         fields = ['workshop_id', 'name', 'date', 'place', 'description', 'completed', 'images', 'videos']

class WorkshopSerializer(serializers.ModelSerializer):
    images = WorkshopImageSerializer(many=True, write_only=True, required=False)
    videos = WorkshopVideoSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Workshop
        fields = [
            'workshop_id', 'name', 'date', 'place', 
            'description', 'completed', 'images', 'videos'
        ]

    def create(self, validated_data):
        images_data = validated_data.pop('new_images', [])
        videos_data = validated_data.pop('videos', [])
        
        # Create the workshop
        workshop = Workshop.objects.create(**validated_data)

        # Create related images
        for image_data in images_data:
            WorkshopImage.objects.create(workshop=workshop, **image_data)

        # Create related videos
        for video_data in videos_data:
            WorkshopVideo.objects.create(workshop=workshop, **video_data)

        return workshop


class NewProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_id', 'name', 'price', 'quantity','discounted_price', 'video_link', 'short_description', 'categories', 'images']

  