import os
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
 
class SaleType(models.Model):
    sale_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    visible = models.BooleanField(default=True)
    header = models.BooleanField(default=False)
    home_page = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='subcategories')
    visible = models.BooleanField(default=True)
    header = models.BooleanField(default=True)
    category_page = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (SubCategory of {self.category.name})"

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    discounted_price = models.IntegerField(default=0, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='products')
    subcategories = models.ManyToManyField(SubCategory, related_name='products', blank=True)
    sale_types = models.ManyToManyField(SaleType, related_name='products')
    video_link = models.URLField(blank=True, null=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CategoryImage(models.Model):
    category_image_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.category.name}"
    
class ProductImage(models.Model):
    product_image_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.product.name}"

class SubCategoryImage(models.Model):
    subcategory_image_id = models.AutoField(primary_key=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.subcategory.name}"
    
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=255)
    rating = models.IntegerField(blank=True, null=True, default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField()
    display = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user_name} on {self.product.name}"

class BannerImage(models.Model):
    banner_image_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = CloudinaryField('image', blank=True, null=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48)
    phone_number = models.CharField(max_length=12, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField()
    pincode = models.CharField(max_length=6)
    visible = models.BooleanField(default=True)
    send_promotion_emails = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField(default=1)
    order_completed = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    note = models.TextField(default="Add a note")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_id} by {self.customer.name}"

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_completed = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
    
class PageContent(models.Model):
    pagecontent_id = models.AutoField(primary_key=True)
    page_name = models.CharField(max_length=32, unique=True)
    content = models.TextField()
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_name

class PageImage(models.Model):
    pageimage_id = models.AutoField(primary_key=True)
    page = models.ForeignKey(PageContent, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image', blank=True, null=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.page.page_name}"
    
class Workshop(models.Model):
    workshop_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField()
    place = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Workshop {self.name} - {self.date} - {self.place}"

class WorkshopImage(models.Model):
    workshopimage_id = models.AutoField(primary_key=True)
    workshop = models.ForeignKey(Workshop, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=True, null=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"Image for Workshop {self.workshop.name}"

class WorkshopVideo(models.Model):
    workshopvideo_id = models.AutoField(primary_key=True)
    workshop = models.ForeignKey(Workshop, related_name='videos', on_delete=models.CASCADE)
    video_url = models.URLField()
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"Video for Workshop {self.workshop.workshop_id}"

