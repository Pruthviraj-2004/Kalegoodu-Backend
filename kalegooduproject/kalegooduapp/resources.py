from import_export import resources
from .models import Customer, Order, OrderItem, SaleType, Category, Product, CategoryImage, ProductImage, Comment, BannerImage

class SaleTypeResource(resources.ModelResource):
    class Meta:
        model = SaleType
        fields = ('sale_type_id', 'name')

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('category_id', 'name', 'description')

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('product_id', 'name', 'price', 'discounted_price', 'short_description')

class CategoryImageResource(resources.ModelResource):
    class Meta:
        model = CategoryImage
        fields = ('category_image_id', 'category', 'image', 'alt_text')

class ProductImageResource(resources.ModelResource):
    class Meta:
        model = ProductImage
        fields = ('product_image_id', 'product', 'image', 'alt_text')

class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment
        fields = ('comment_id', 'product', 'user_name', 'rating', 'text')

class BannerImageResource(resources.ModelResource):
    class Meta:
        model = BannerImage
        fields = ('banner_image_id', 'title', 'image')

class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
        fields = ('customer_id', 'name', 'phone_number', 'email', 'address', 'pincode')

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        fields = ('order_id', 'customer__name', 'count', 'total_amount')

class OrderItemResource(resources.ModelResource):
    class Meta:
        model = OrderItem
        fields = ('order_item_id', 'order__order_id', 'product__name', 'quantity', 'price')
