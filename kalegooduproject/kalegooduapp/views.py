from django.shortcuts import render

def home(request):
    return render(request, 'kalegooduapp/home.html')

from rest_framework import viewsets
from .models import Category, Product, ProductImage, CategoryImage, Comment
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer, CategoryImageSerializer, CommentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class CategoryImageViewSet(viewsets.ModelViewSet):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
