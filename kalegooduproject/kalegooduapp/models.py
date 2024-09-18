from django.utils import timezone
import os
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import shutil
from django.conf import settings

def product_image_upload_path(instance, filename):
    # Create a dynamic path: 'product_images/<product_name>/<filename>'
    return os.path.join('product_images', instance.product.name, filename)

def category_image_upload_path(instance, filename):
    # Create a dynamic path: 'category_images/<category_name>/<filename>'
    return os.path.join('category_images', instance.category.name, filename)
    
class SaleType(models.Model):
    sale_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    discounted_price = models.IntegerField(default=0, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='products')
    sale_types = models.ManyToManyField(SaleType, related_name='products')
    video_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CategoryImage(models.Model):
    category_image_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=category_image_upload_path)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.category.name}"
    
class ProductImage(models.Model):
    product_image_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=product_image_upload_path)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.product.name}"

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

def banner_image_upload_path(instance, filename):
    return os.path.join('banner_images', filename)

class BannerImage(models.Model):
    banner_image_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=banner_image_upload_path)
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
    
class PageContent(models.Model):
    pagecontent_id = models.AutoField(primary_key=True)
    page_name = models.CharField(max_length=32, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_name
    
def page_image_upload_path(instance, filename):
    return os.path.join('page_images', instance.page.page_name, filename)

class PageImage(models.Model):
    pageimage_id = models.AutoField(primary_key=True)
    page = models.ForeignKey(PageContent, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=page_image_upload_path, blank=True, null=True)
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

def workshop_image_upload_path(instance, filename):
    return os.path.join('workshop_images', instance.workshop.name, filename)

class WorkshopImage(models.Model):
    workshopimage_id = models.AutoField(primary_key=True)
    workshop = models.ForeignKey(Workshop, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=workshop_image_upload_path, blank=True, null=True)

    def __str__(self):
        return f"Image for Workshop {self.workshop.name}"

class WorkshopVideo(models.Model):
    workshopvideo_id = models.AutoField(primary_key=True)
    workshop = models.ForeignKey(Workshop, related_name='videos', on_delete=models.CASCADE)
    video_url = models.URLField()

    def __str__(self):
        return f"Video for Workshop {self.workshop.workshop_id}"