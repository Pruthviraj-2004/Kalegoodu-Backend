from django.shortcuts import render

def home(request):
    return render(request, 'kalegooduapp/home.html')

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, SaleType, Product, ProductImage, CategoryImage, Comment
from .serializers import CategorySerializer, SaleTypeSerializer, ProductSerializer, ProductImageSerializer, CategoryImageSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({'categories': serializer.data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'category': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SaleTypeView(APIView):
    def get(self, request):
        sale_types = SaleType.objects.all()
        serializer = SaleTypeSerializer(sale_types, many=True)
        return Response({'sale_types': serializer.data})

    def post(self, request):
        serializer = SaleTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'sale_type': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'product': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductImageView(APIView):
    def get(self, request):
        product_images = ProductImage.objects.all()
        serializer = ProductImageSerializer(product_images, many=True)
        return Response({'product_images': serializer.data})

    def post(self, request):
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'product_image': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryImageView(APIView):
    def get(self, request):
        category_images = CategoryImage.objects.all()
        serializer = CategoryImageSerializer(category_images, many=True)
        return Response({'category_images': serializer.data})

    def post(self, request):
        serializer = CategoryImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'category_image': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response({'comments': serializer.data})

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'comment': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailAPIView(APIView):
    def get(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        serializer = CategorySerializer(category)
        return Response({'category': serializer.data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'category': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SaleTypeDetailAPIView(APIView):
    def get(self, request, sale_type_id):
        sale_type = get_object_or_404(SaleType, pk=sale_type_id)
        serializer = SaleTypeSerializer(sale_type)
        return Response({'sale_type': serializer.data})

    def post(self, request):
        serializer = SaleTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'sale_type': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        serializer = ProductSerializer(product)
        return Response({'product': serializer.data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'product': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductImageDetailAPIView(APIView):
    def get(self, request, product_image_id):
        product_image = get_object_or_404(ProductImage, pk=product_image_id)
        serializer = ProductImageSerializer(product_image)
        return Response({'product_image': serializer.data})

    def post(self, request):
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'product_image': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryImageDetailAPIView(APIView):
    def get(self, request, category_image_id):
        category_image = get_object_or_404(CategoryImage, pk=category_image_id)
        serializer = CategoryImageSerializer(category_image)
        return Response({'category_image': serializer.data})

    def post(self, request):
        serializer = CategoryImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'category_image': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailAPIView(APIView):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        serializer = CommentSerializer(comment)
        return Response({'comment': serializer.data})

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'comment': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
