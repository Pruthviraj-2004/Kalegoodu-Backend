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
    
    def delete(self, *args, **kwargs):
        print("Custom delete method called")
        path = os.path.join(settings.MEDIA_ROOT, 'category_images', self.name)
        print("Deleting path:", path)
        super(Category, self).delete(*args, **kwargs)
        if os.path.isdir(path):
            shutil.rmtree(path)
        print("Deletion complete")

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
    
    def delete(self, *args, **kwargs):
        print("Custom delete method called for product")
        path = os.path.join(settings.MEDIA_ROOT, 'product_images', self.name)
        print("Deleting path:", path)
        super(Product, self).delete(*args, **kwargs)
        if os.path.isdir(path):
            shutil.rmtree(path)
        print("Deletion complete")

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