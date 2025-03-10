from django.conf import settings
from rest_framework import serializers
from .models import BannerImage, Category, Customer, Order, OrderItem, PageContent, PageImage, SaleType, Product, ProductImage, CategoryImage, Comment, SubCategory, SubCategoryImage, Workshop, WorkshopImage, WorkshopVideo

class SaleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleType
        fields = ['sale_type_id', 'name', 'visible']

class CategoryImageSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = CategoryImage
        fields = ['category_image_id', 'category', 'category_name', 'image', 'visible', 'alt_text']


class SimpleCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['category_id', 'name', 'visible', 'header', 'home_page']

class ProductImageSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = ProductImage
        fields = ['product_image_id', 'product', 'product_name', 'image', 'visible', 'alt_text']

class CommentSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Comment
        fields = ['comment_id', 'product', 'product_name', 'user_name', 'text', 'rating', 'display']

class SubCategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryImage
        fields = ['subcategory_image_id', 'image', 'alt_text', 'visible']

class SimpleSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['subcategory_id', 'name', 'visible', 'header', 'category_page']

class NavbarSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['subcategory_id', 'name']

class NavbarCategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['category_id', 'name', 'subcategories']

    def get_subcategories(self, obj):
        subcategories = obj.subcategories.filter(visible=True, header=True)
        return NavbarSubCategorySerializer(subcategories, many=True).data

class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = SubCategory
        fields = ['subcategory_id', 'name', 'description', 'category', 'visible', 'header', 'category_page', 'images']

    def get_images(self, obj):
        images = SubCategoryImage.objects.filter(subcategory=obj)
        return SubCategoryImageSerializer(images, many=True).data

    def get_products(self, obj):
        products = obj.products.filter(visible=True)
        return ProductSerializer(products, many=True).data

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SimpleSubCategorySerializer(many=True, read_only=True)
    images = CategoryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_id', 'name', 'visible', 'header', 'home_page', 'description', 'subcategories','images']

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    subcategories = SubCategorySerializer(many=True, read_only=True)
    sale_types = SaleTypeSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_id', 'name', 'price', 'quantity','discounted_price', 'visible', 'video_link', 'short_description', 'categories', 'subcategories', 'sale_types', 'images', 'comments','created_at']

class SubCategoryWithProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ['subcategory_id', 'name', 'products']

class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ['banner_image_id', 'title', 'image', 'visible']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id','name','phone_number','pincode','email','address']

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['order_item_id', 'order', 'product', 'product_name', 'quantity', 'price', 'order_completed', 'visible']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    customer_name = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = Order
        fields = ['order_id', 'customer', 'customer_name', 'total_amount', 'count', 'order_completed', 'visible', 'note', 'created_at', 'updated_at', 'items']

class PageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageImage
        fields = ['pageimage_id', 'image', 'visible', 'created_at', 'updated_at']

class PageContentSerializer(serializers.ModelSerializer):
    images = PageImageSerializer(many=True, read_only=True)

    class Meta:
        model = PageContent
        fields = ['pagecontent_id', 'page_name', 'content', 'visible', 'created_at', 'updated_at', 'images']

class WorkshopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopImage
        fields = ['workshopimage_id', 'image', 'visible']

class AddWorkshopImageSerializer(serializers.ModelSerializer):
    workshop_name = serializers.CharField(source='workshop.name', read_only=True)

    class Meta:
        model = WorkshopImage
        fields = ['workshopimage_id', 'workshop', 'workshop_name', 'image', 'visible']

class WorkshopVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopVideo
        fields = ['workshopvideo_id', 'video_url', 'visible']

class AddWorkshopVideoSerializer(serializers.ModelSerializer):
    workshop_name = serializers.CharField(source='workshop.name', read_only=True)

    class Meta:
        model = WorkshopVideo
        fields = ['workshopvideo_id', 'workshop', 'workshop_name', 'video_url', 'visible']

class WorkshopSerializer(serializers.ModelSerializer):
    images = AddWorkshopImageSerializer(many=True, read_only=True)
    videos = AddWorkshopVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Workshop
        fields = ['workshop_id', 'name', 'date', 'place', 'description', 'completed', 'images', 'videos']

class AddWorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = ['workshop_id', 'name', 'date', 'place', 'description', 'completed']

class NewProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    subcategories = SubCategorySerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_id', 'name', 'price', 'quantity','discounted_price', 'video_link', 'short_description', 'categories', 'subcategories', 'images', 'visible']

class ProductImageTestimonialSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['image_url']

    def get_image_url(self, obj):
        # return f"https://res.cloudinary.com/dgkgxokru/{obj.image}" if obj.image else None
        return f"https://res.cloudinary.com/{settings.CLOUD_NAME}/{obj.image}" if obj.image else None

class ProductTestimonialSerializer(serializers.ModelSerializer):
    images = ProductImageTestimonialSerializer(many=True)

    class Meta:
        model = Product
        fields = ['product_id', 'name', 'images', 'price','discounted_price', 'quantity']
