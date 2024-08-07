from django.shortcuts import render

def home(request):
    return render(request, 'kalegooduapp/home.html')

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BannerImage, Category, SaleType, Product, ProductImage, CategoryImage, Comment
from .serializers import BannerImageSerializer, CategorySerializer, SaleTypeSerializer, ProductSerializer, ProductImageSerializer, CategoryImageSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import status
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
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

@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(APIView):
    @transaction.atomic
    def post(self, request):
        category_data = {
            'name': request.data.get('name'),
            'description': request.data.get('description')
        }
        category_serializer = CategorySerializer(data=category_data)

        if category_serializer.is_valid():
            category = category_serializer.save()

            images = request.FILES.getlist('images')
            for image in images:
                category_image_data = {
                    'category': category.category_id,
                    'image': image,
                    'alt_text': request.data.get('alt_text', '')
                }
                category_image_serializer = CategoryImageSerializer(data=category_image_data)
                if category_image_serializer.is_valid():
                    category_image_serializer.save()
                else:
                    transaction.set_rollback(True)
                    return Response(category_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'category': category_serializer.data}, status=status.HTTP_201_CREATED)

        return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class ProductCreateView(APIView):
    @transaction.atomic
    def post(self, request):
        product_data = {
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'discounted_price': request.data.get('discounted_price', '0'),
            'short_description': request.data.get('short_description')
        }

        # Parse categories and sale_types from string to list
        categories_data = request.data.get('categories', '[]')
        sale_types_data = request.data.get('sale_types', '[]')

        try:
            if isinstance(categories_data, str):
                categories_data = json.loads(categories_data)
            if isinstance(sale_types_data, str):
                sale_types_data = json.loads(sale_types_data)
        except json.JSONDecodeError:
            return Response({'error': 'Invalid data format for categories or sale types.'}, status=status.HTTP_400_BAD_REQUEST)

        images_data = request.FILES.getlist('images')

        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product = product_serializer.save()

            # Adding categories
            if categories_data:
                for category_id in categories_data:
                    try:
                        category = Category.objects.get(pk=int(category_id))
                        product.categories.add(category)
                    except (Category.DoesNotExist, ValueError):
                        transaction.set_rollback(True)
                        return Response(
                            {'error': f'Category with ID {category_id} does not exist or invalid.'},
                            status=status.HTTP_400_BAD_REQUEST
                        )

            # Adding sale types
            if sale_types_data:
                for sale_type_id in sale_types_data:
                    try:
                        sale_type = SaleType.objects.get(pk=int(sale_type_id))
                        product.sale_types.add(sale_type)
                    except (SaleType.DoesNotExist, ValueError):
                        transaction.set_rollback(True)
                        return Response(
                            {'error': f'SaleType with ID {sale_type_id} does not exist or invalid.'},
                            status=status.HTTP_400_BAD_REQUEST
                        )

            # Adding images
            for image in images_data:
                product_image_data = {
                    'product': product.product_id,
                    'image': image,
                    'alt_text': request.data.get('alt_text', '')
                }
                product_image_serializer = ProductImageSerializer(data=product_image_data)
                if product_image_serializer.is_valid():
                    product_image_serializer.save()
                else:
                    product.delete()
                    transaction.set_rollback(True)
                    return Response(product_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'product': product_serializer.data}, status=status.HTTP_201_CREATED)

        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@method_decorator(csrf_exempt, name='dispatch')
class BannerImageView(APIView):
    def get(self, request):
        banner_images = BannerImage.objects.all()
        serializer = BannerImageSerializer(banner_images, many=True)
        return Response({'banner_images': serializer.data})

    def post(self, request):
        image = request.FILES.get('image')
        title = request.data.get('title')

        if not image:
            return Response({'error': 'No image file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        banner_image_data = {
            'title': title,
            'image': image
        }
        
        serializer = BannerImageSerializer(data=banner_image_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'banner_image': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductsByCategoryView(APIView):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)

        products = category.products.all()
        serializer = ProductSerializer(products, many=True)

        return Response({'products': serializer.data}, status=status.HTTP_200_OK)
    
class CategoriesByProduct(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(product_id=product_id)
            categories = product.categories.all()
            serializer = CategorySerializer(categories, many=True)
            return Response({'categories': serializer.data}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
    


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(APIView):
    def put(self, request, category_id):
        try:
            category = Category.objects.get(category_id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)

        category_data = {
            'name': request.data.get('name', category.name),
            'description': request.data.get('description', category.description)
        }
        category_serializer = CategorySerializer(category, data=category_data, partial=True)

        if category_serializer.is_valid():
            category_serializer.save()
            return Response({'category': category_serializer.data}, status=status.HTTP_200_OK)
        
        return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@method_decorator(csrf_exempt, name='dispatch')
class CategoryImageUpdateView(APIView):
    def put(self, request, image_id):
        try:
            category_image = CategoryImage.objects.get(category_image_id=image_id)
        except CategoryImage.DoesNotExist:
            return Response({'error': 'Category image not found.'}, status=status.HTTP_404_NOT_FOUND)

        category_image_data = {
            'category': request.data.get('category', category_image.category.category_id),
            'alt_text': request.data.get('alt_text', category_image.alt_text)
        }

        if 'image' in request.FILES:
            category_image_data['image'] = request.FILES['image']
        
        category_image_serializer = CategoryImageSerializer(category_image, data=category_image_data, partial=True)

        if category_image_serializer.is_valid():
            category_image_serializer.save()
            return Response({'category_image': category_image_serializer.data}, status=status.HTTP_200_OK)
        
        return Response(category_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@method_decorator(csrf_exempt, name='dispatch')
class FullCategoryUpdateView(APIView):
    @transaction.atomic
    def put(self, request, category_id):
        try:
            category = Category.objects.get(category_id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)

        category_data = {
            'name': request.data.get('name', category.name),
            'description': request.data.get('description', category.description)
        }
        category_serializer = CategorySerializer(category, data=category_data, partial=True)

        if not category_serializer.is_valid():
            return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        category_serializer.save()

        # Update existing images
        image_updates = request.data.get('images', '[]')
        for image_update in image_updates:
            image_id = image_update.get('id')
            if image_id:
                try:
                    category_image = CategoryImage.objects.get(category_image_id=image_id, category=category)
                except CategoryImage.DoesNotExist:
                    continue  # Skip images not found

                category_image_data = {
                    'alt_text': image_update.get('alt_text', category_image.alt_text),
                }

                if 'image' in image_update:
                    category_image_data['image'] = image_update['image']

                category_image_serializer = CategoryImageSerializer(category_image, data=category_image_data, partial=True)
                if category_image_serializer.is_valid():
                    category_image_serializer.save()
                else:
                    transaction.set_rollback(True)
                    return Response(category_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Add new images
        new_images = request.FILES.getlist('new_images')
        for image in new_images:
            category_image_data = {
                'category': category.category_id,
                'image': image,
                'alt_text': request.data.get('alt_text', '')
            }
            category_image_serializer = CategoryImageSerializer(data=category_image_data)
            if category_image_serializer.is_valid():
                category_image_serializer.save()
            else:
                transaction.set_rollback(True)
                return Response(category_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'category': category_serializer.data}, status=status.HTTP_200_OK)
       
@method_decorator(csrf_exempt, name='dispatch')
class ProductUpdateView(APIView):
    def put(self, request, product_id):
        try:
            product = Product.objects.get(product_id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        product_data = {
            'name': request.data.get('name', product.name),
            'price': request.data.get('price', product.price),
            'discounted_price': request.data.get('discounted_price', product.discounted_price),
            'short_description': request.data.get('short_description', product.short_description),
        }
        product_serializer = ProductSerializer(product, data=product_data, partial=True)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'product': product_serializer.data}, status=status.HTTP_200_OK)

        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@method_decorator(csrf_exempt, name='dispatch')
class ProductImageUpdateView(APIView):
    def put(self, request, image_id):
        try:
            product_image = ProductImage.objects.get(product_image_id=image_id)
        except ProductImage.DoesNotExist:
            return Response({'error': 'Product image not found.'}, status=status.HTTP_404_NOT_FOUND)

        product_image_data = {
            'product': request.data.get('product', product_image.product.product_id),
            'alt_text': request.data.get('alt_text', product_image.alt_text)
        }

        if 'image' in request.FILES:
            product_image_data['image'] = request.FILES['image']

        product_image_serializer = ProductImageSerializer(product_image, data=product_image_data, partial=True)

        if product_image_serializer.is_valid():
            product_image_serializer.save()
            return Response({'product_image': product_image_serializer.data}, status=status.HTTP_200_OK)

        return Response(product_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class ProductFullUpdateView(APIView):
    @transaction.atomic
    def put(self, request, product_id):
        try:
            product = Product.objects.get(product_id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Update Product Information
        product_data = {
            'name': request.data.get('name', product.name),
            'price': request.data.get('price', product.price),
            'discounted_price': request.data.get('discounted_price', product.discounted_price),
            'short_description': request.data.get('short_description', product.short_description),
        }
        product_serializer = ProductSerializer(product, data=product_data, partial=True)

        if not product_serializer.is_valid():
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        product_serializer.save()

        # Update Product Images
        image_updates = request.data.get('images', '[]')
        
        # Process existing images
        for image_update in image_updates:
            image_id = image_update.get('id')
            if image_id:
                try:
                    product_image = ProductImage.objects.get(product_image_id=image_id, product=product)
                except ProductImage.DoesNotExist:
                    continue  # Skip images not found

                product_image_data = {
                    'alt_text': image_update.get('alt_text', product_image.alt_text),
                }

                if 'image' in image_update:
                    product_image_data['image'] = image_update['image']
                
                product_image_serializer = ProductImageSerializer(product_image, data=product_image_data, partial=True)
                if product_image_serializer.is_valid():
                    product_image_serializer.save()
                else:
                    transaction.set_rollback(True)
                    return Response(product_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Process new images
        new_images = request.FILES.getlist('new_images')
        for image in new_images:
            product_image_data = {
                'product': product.product_id,
                'image': image,
                'alt_text': request.data.get('alt_text', '')
            }
            product_image_serializer = ProductImageSerializer(data=product_image_data)
            if product_image_serializer.is_valid():
                product_image_serializer.save()
            else:
                transaction.set_rollback(True)
                return Response(product_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'product': product_serializer.data}, status=status.HTTP_200_OK)

@method_decorator(csrf_exempt, name='dispatch')
class SaleTypeUpdateView(APIView):
    def put(self, request, sale_type_id):
        try:
            sale_type = SaleType.objects.get(sale_type_id=sale_type_id)
        except SaleType.DoesNotExist:
            return Response({'error': 'SaleType not found.'}, status=status.HTTP_404_NOT_FOUND)

        sale_type_data = {
            'name': request.data.get('name', sale_type.name)
        }
        sale_type_serializer = SaleTypeSerializer(sale_type, data=sale_type_data, partial=True)

        if sale_type_serializer.is_valid():
            sale_type_serializer.save()
            return Response({'sale_type': sale_type_serializer.data}, status=status.HTTP_200_OK)

        return Response(sale_type_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class CommentUpdateView(APIView):
    def put(self, request, comment_id):
        try:
            comment = Comment.objects.get(comment_id=comment_id)
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found.'}, status=status.HTTP_404_NOT_FOUND)

        comment_data = {
            'product': request.data.get('product', comment.product.product_id),
            'user_name': request.data.get('user_name', comment.user_name),
            'rating': request.data.get('rating', comment.rating),
            'text': request.data.get('text', comment.text)
        }
        comment_serializer = CommentSerializer(comment, data=comment_data, partial=True)

        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response({'comment': comment_serializer.data}, status=status.HTTP_200_OK)

        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class BannerImageUpdateView(APIView):
    def put(self, request, banner_image_id):
        try:
            banner_image = BannerImage.objects.get(banner_image_id=banner_image_id)
        except BannerImage.DoesNotExist:
            return Response({'error': 'BannerImage not found.'}, status=status.HTTP_404_NOT_FOUND)

        banner_image_data = {
            'title': request.data.get('title', banner_image.title),
            'image': request.FILES.get('image', banner_image.image)
        }
        serializer = BannerImageSerializer(banner_image, data=banner_image_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'banner_image': serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class AddCategoryImageView(APIView):
    def post(self, request, category_id):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)

        image = request.FILES.get('image')
        alt_text = request.data.get('alt_text', '')

        if not image:
            return Response({'error': 'No image file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        category_image_data = {
            'category': category_id,
            'image': image,
            'alt_text': alt_text
        }
        category_image_serializer = CategoryImageSerializer(data=category_image_data)

        if category_image_serializer.is_valid():
            category_image_serializer.save()
            return Response({'category_image': category_image_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(category_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@method_decorator(csrf_exempt, name='dispatch')
class AddProductImageView(APIView):
    def post(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        image = request.FILES.get('image')
        alt_text = request.data.get('alt_text', '')

        if not image:
            return Response({'error': 'No image file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        product_image_data = {
            'product': product_id,
            'image': image,
            'alt_text': alt_text
        }
        product_image_serializer = ProductImageSerializer(data=product_image_data)

        if product_image_serializer.is_valid():
            product_image_serializer.save()
            return Response({'product_image': product_image_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(product_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@method_decorator(csrf_exempt, name='dispatch')
class SaleTypeDeleteView(APIView):
    def delete(self, request, sale_type_id):
        try:
            sale_type = SaleType.objects.get(pk=sale_type_id)
            sale_type.delete()
            return Response({'message': 'SaleType deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except SaleType.DoesNotExist:
            return Response({'error': 'SaleType not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(APIView):
    def delete(self, request, category_id):
        try:
            category = Category.objects.get(pk=category_id)
            category.delete()
            return Response({'message': 'Category deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class ProductDeleteView(APIView):
    def delete(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
            product.delete()
            return Response({'message': 'Product deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class CategoryImageDeleteView(APIView):
    def delete(self, request, category_image_id):
        try:
            category_image = CategoryImage.objects.get(pk=category_image_id)
            category_image.delete()
            return Response({'message': 'Category image deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except CategoryImage.DoesNotExist:
            return Response({'error': 'Category image not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class ProductImageDeleteView(APIView):
    def delete(self, request, product_image_id):
        try:
            product_image = ProductImage.objects.get(pk=product_image_id)
            product_image.delete()
            return Response({'message': 'Product image deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except ProductImage.DoesNotExist:
            return Response({'error': 'Product image not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class CommentDeleteView(APIView):
    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(pk=comment_id)
            comment.delete()
            return Response({'message': 'Comment deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class BannerImageDeleteView(APIView):
    def delete(self, request, banner_image_id):
        try:
            banner_image = BannerImage.objects.get(pk=banner_image_id)
            banner_image.delete()
            return Response({'message': 'Banner image deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except BannerImage.DoesNotExist:
            return Response({'error': 'Banner image not found.'}, status=status.HTTP_404_NOT_FOUND)
        
