from django.shortcuts import render

def home(request):
    return render(request, 'kalegooduapp/home.html')

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BannerImage, Category, PageContent, PageImage, SaleType, Product, ProductImage, CategoryImage, Comment, Customer, Order, OrderItem, Workshop, WorkshopImage, WorkshopVideo
from .serializers import BannerImageSerializer, CategorySerializer, PageContentSerializer, PageImageSerializer, SaleTypeSerializer, ProductSerializer, ProductImageSerializer, CategoryImageSerializer, CommentSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer, WorkshopImageSerializer, WorkshopSerializer, WorkshopVideoSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import status
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.http import JsonResponse
from .utils import send_whatsapp_message

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.files.storage import default_storage

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
class CustomerView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({'customers': serializer.data})

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class OrderView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({'orders': serializer.data})

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'order': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class OrderItemView(APIView):
    def get(self, request):
        order_items = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return Response({'order_items': serializer.data})

    def post(self, request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'order_item': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class OrderDetailAPIView(APIView):
    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serializer = OrderSerializer(order)
        return Response({'order': serializer.data})

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'order': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class CustomerDetailAPIView(APIView):
    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, pk=customer_id)
        serializer = CustomerSerializer(customer)
        return Response({'customer': serializer.data})

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailWithCustomerAPIView(APIView):
    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)

        order_serializer = OrderSerializer(order)
        customer_serializer = CustomerSerializer(order.customer)

        return Response({'customer': customer_serializer.data,'order': order_serializer.data})

class PageContentListView(APIView):
    def get(self, request):
        page_contents = PageContent.objects.all()
        serializer = PageContentSerializer(page_contents, many=True)
        return Response({'page_contents': serializer.data}, status=status.HTTP_200_OK)

class PageContentDetailView(APIView):
    def get(self, request, pagecontent_id):
        page_content = get_object_or_404(PageContent, pk=pagecontent_id)
        serializer = PageContentSerializer(page_content)
        return Response({'page_content': serializer.data}, status=status.HTTP_200_OK)

class PageImageListView(APIView):
    def get(self, request):
        page_images = PageImage.objects.all()
        serializer = PageImageSerializer(page_images, many=True)
        return Response({'page_images': serializer.data}, status=status.HTTP_200_OK)

class PageImageDetailView(APIView):
    def get(self, request, pageimage_id):
        page_image = get_object_or_404(PageImage, pk=pageimage_id)
        serializer = PageImageSerializer(page_image)
        return Response({'page_image': serializer.data}, status=status.HTTP_200_OK)

class WorkshopListView(APIView):
    def get(self, request):
        workshops = Workshop.objects.all()
        serializer = WorkshopSerializer(workshops, many=True)
        return Response({'workshops': serializer.data}, status=status.HTTP_200_OK)

class WorkshopDetailView(APIView):
    def get(self, request, workshop_id):
        workshop = get_object_or_404(Workshop, pk=workshop_id)
        serializer = WorkshopSerializer(workshop)
        return Response({'workshop': serializer.data}, status=status.HTTP_200_OK)

class WorkshopImageListView(APIView):
    def get(self, request):
        workshop_images = WorkshopImage.objects.all()
        serializer = WorkshopImageSerializer(workshop_images, many=True)
        return Response({'workshop_images': serializer.data}, status=status.HTTP_200_OK)

class WorkshopImageDetailView(APIView):
    def get(self, request, workshop_image_id):
        workshop_image = get_object_or_404(WorkshopImage, pk=workshop_image_id)
        serializer = WorkshopImageSerializer(workshop_image)
        return Response({'workshop_image': serializer.data}, status=status.HTTP_200_OK)

class WorkshopVideoListView(APIView):
    def get(self, request):
        workshop_videos = WorkshopVideo.objects.all()
        serializer = WorkshopVideoSerializer(workshop_videos, many=True)
        return Response({'workshop_videos': serializer.data}, status=status.HTTP_200_OK)

class WorkshopVideoDetailView(APIView):
    def get(self, request, workshop_video_id):
        workshop_video = get_object_or_404(WorkshopVideo, pk=workshop_video_id)
        serializer = WorkshopVideoSerializer(workshop_video)
        return Response({'workshop_video': serializer.data}, status=status.HTTP_200_OK)

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
            'short_description': request.data.get('short_description'),
            'quantity': request.data.get('quantity'),
            'video_link': request.data.get('video_link')
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

@method_decorator(csrf_exempt, name='dispatch')
class PageContentCreateView(APIView):
    @transaction.atomic
    def post(self, request):
        page_content_data = {
            'page_name': request.data.get('page_name'),
            'content': request.data.get('content')
        }
        page_content_serializer = PageContentSerializer(data=page_content_data)

        if page_content_serializer.is_valid():
            page_content = page_content_serializer.save()

            page_images = request.FILES.getlist('page_image')
            for image in page_images:
                page_image_data = {
                    'page': page_content.pagecontent_id,
                    'image': image,
                }
                page_image_serializer = PageImageSerializer(data=page_image_data)
                if page_image_serializer.is_valid():
                    page_image_serializer.save()
                else:
                    transaction.set_rollback(True)
                    return Response(page_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'page_content': page_content_serializer.data}, status=status.HTTP_201_CREATED)

        return Response(page_content_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
class WorkshopCreateView(APIView):
    @transaction.atomic
    def post(self, request):
        # Extract workshop data
        workshop_data = {
            'name': request.data.get('name'),
            'date': request.data.get('date'),
            'place': request.data.get('place'),
            'description': request.data.get('description')
        }
        workshop_serializer = WorkshopSerializer(data=workshop_data)

        if workshop_serializer.is_valid():
            workshop = workshop_serializer.save()

            # Handle uploaded images
            images = request.FILES.getlist('images')
            for image in images:
                workshop_image_data = {
                    'workshop': workshop,  # Pass the Workshop instance directly
                    'image': image
                }
                workshop_image_serializer = WorkshopImageSerializer(data=workshop_image_data)
                if workshop_image_serializer.is_valid():
                    workshop_image_serializer.save(workshop=workshop)
                else:
                    transaction.set_rollback(True)
                    return Response(workshop_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Handle video URL if provided
            video_url = request.data.get('video_url')
            print(video_url)
            if video_url:
                workshop_video_serializer = WorkshopVideoSerializer(data={'video_url': video_url})
                if workshop_video_serializer.is_valid():
                    workshop_video_serializer.save(workshop=workshop)  # Pass the Workshop instance here
                else:
                    transaction.set_rollback(True)
                    return Response(workshop_video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'workshop': workshop_serializer.data}, status=status.HTTP_201_CREATED)

        return Response(workshop_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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

        # Add new images
        new_images = request.FILES.getlist('new_images')
        print(request.data)
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
            'video_link': request.data.get('video_link', product.video_link),
            'quantity': request.data.get('quantity', product.quantity)
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
            'video_link': request.data.get('video_link', product.video_link),
            'quantity': request.data.get('quantity', product.quantity)
        }
        product_serializer = ProductSerializer(product, data=product_data, partial=True)

        if not product_serializer.is_valid():
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        product_serializer.save()

        # Update Categories
        categories_data = request.data.get('categories', '[]')
        try:
            if isinstance(categories_data, str):
                categories_data = json.loads(categories_data)
            categories = Category.objects.filter(category_id__in=categories_data)
            product.categories.set(categories)

        except Category.DoesNotExist:
            transaction.set_rollback(True)
            return Response({'error': 'One or more categories not found.'}, status=status.HTTP_400_BAD_REQUEST)

        # Update Sale Types
        sale_types_data = request.data.get('sale_types', '[]')
        try:
            if isinstance(sale_types_data, str):
                sale_types_data = json.loads(sale_types_data)
            sale_types = SaleType.objects.filter(sale_type_id__in=sale_types_data)
            product.sale_types.set(sale_types)

        except SaleType.DoesNotExist:
            transaction.set_rollback(True)
            return Response({'error': 'One or more sale types not found.'}, status=status.HTTP_400_BAD_REQUEST)

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
class FullPageContentUpdateView(APIView):
    @transaction.atomic
    def put(self, request, page_content_id):
        try:
            page_content = PageContent.objects.get(pk=page_content_id)
        except PageContent.DoesNotExist:
            return Response({'error': 'Page content not found.'}, status=status.HTTP_404_NOT_FOUND)

        page_content_data = {
            'page_name': request.data.get('page_name', page_content.page_name),
            'content': request.data.get('content', page_content.content)
        }
        page_content_serializer = PageContentSerializer(page_content, data=page_content_data, partial=True)

        if not page_content_serializer.is_valid():
            return Response(page_content_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        page_content_serializer.save()

        new_images = request.FILES.getlist('new_images')
        for image in new_images:
            page_image_data = {
                'page': page_content.pagecontent_id,
                'image': image,
            }
            page_image_serializer = PageImageSerializer(data=page_image_data)
            if page_image_serializer.is_valid():
                page_image_serializer.save()
            else:
                transaction.set_rollback(True)
                return Response(page_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'page_content': page_content_serializer.data}, status=status.HTTP_200_OK)

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
class CustomerUpdateView(APIView):
    def put(self, request, customer_id):
        try:
            customer = Customer.objects.get(customer_id=customer_id)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)

        customer_data = {
            'name': request.data.get('name', customer.name),
            'phone_number': request.data.get('phone_number', customer.phone_number),
            'email': request.data.get('email', customer.email),
            'address': request.data.get('address', customer.address),
            'pincode': request.data.get('pincode', customer.pincode),
        }
        customer_serializer = CustomerSerializer(customer, data=customer_data, partial=True)

        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response({'customer': customer_serializer.data}, status=status.HTTP_200_OK)

        return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class OrderUpdateView(APIView):
    def put(self, request, order_id):
        try:
            order = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)

        order_data = {
            'total_amount': request.data.get('total_amount', order.total_amount),
            'count': request.data.get('count', order.count),
        }
        order_serializer = OrderSerializer(order, data=order_data, partial=True)

        if order_serializer.is_valid():
            order_serializer.save()
            return Response({'order': order_serializer.data}, status=status.HTTP_200_OK)

        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class OrderItemUpdateView(APIView):
    def put(self, request, order_item_id):
        try:
            order_item = OrderItem.objects.get(order_item_id=order_item_id)
        except OrderItem.DoesNotExist:
            return Response({'error': 'OrderItem not found.'}, status=status.HTTP_404_NOT_FOUND)

        order_item_data = {
            'quantity': request.data.get('quantity', order_item.quantity),
            'price': request.data.get('price', order_item.price),
        }
        order_item_serializer = OrderItemSerializer(order_item, data=order_item_data, partial=True)

        if order_item_serializer.is_valid():
            order_item_serializer.save()
            return Response({'order_item': order_item_serializer.data}, status=status.HTTP_200_OK)

        return Response(order_item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateOrderView(APIView):
    @transaction.atomic
    def put(self, request):
        try:
            data = json.loads(request.body)
            order_id = data.get('order_id')
            order_items_data = data.get('items')

            order = Order.objects.get(order_id=order_id)

            total_amount = sum(item.price for item in order.items.all())
            total_count = sum(item.quantity for item in order.items.all())

            for item_data in order_items_data:
                product_id = item_data.get('product_id')
                new_quantity = item_data.get('quantity')

                if not product_id or not new_quantity:
                    return Response({'error': 'Invalid product or quantity.'}, status=status.HTTP_400_BAD_REQUEST)

                try:
                    product = Product.objects.get(product_id=product_id)
                except Product.DoesNotExist:
                    return Response({'error': f"Product {product_id} not found."}, status=status.HTTP_404_NOT_FOUND)

                if new_quantity > product.quantity:
                    return Response({
                        'error': f"Insufficient stock for product {product.name}. Available quantity: {product.quantity}"
                    }, status=status.HTTP_400_BAD_REQUEST)

                try:
                    order_item = OrderItem.objects.get(order=order, product_id=product_id)

                    total_amount -= order_item.price
                    total_count -= order_item.quantity

                    order_item.quantity = new_quantity
                    order_item.price = product.price * new_quantity
                    order_item.order_completed = True
                    order_item.save()

                    total_amount += order_item.price
                    total_count += order_item.quantity
                except OrderItem.DoesNotExist:
                    return Response({'error': f"Order item for product {product_id} not found."}, status=status.HTTP_404_NOT_FOUND)

            order.count = total_count
            order.total_amount = total_amount

            if all(item.order_completed for item in order.items.all()):
                order.order_completed = True
            else:
                order.order_completed = False

            order.save()

            return Response({'message': 'Order and items updated successfully.'}, status=status.HTTP_200_OK)

        except Order.DoesNotExist:
            return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON data.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            transaction.set_rollback(True)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@method_decorator(csrf_exempt, name='dispatch')
class WorkshopUpdateView(APIView):
    def put(self, request, workshop_id):
        try:
            workshop = Workshop.objects.get(workshop_id=workshop_id)
        except Workshop.DoesNotExist:
            return Response({'error': 'Workshop not found.'}, status=status.HTTP_404_NOT_FOUND)

        workshop_data = {
            'name': request.data.get('name', workshop.name),
            'date': request.data.get('date', workshop.date),
            'place': request.data.get('place', workshop.place),
            'description': request.data.get('description', workshop.description)
        }
        workshop_serializer = WorkshopSerializer(workshop, data=workshop_data, partial=True)

        if not workshop_serializer.is_valid():
            return Response(workshop_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        workshop_serializer.save()

        videos_data = request.data.get('videos', '[]')

        if isinstance(videos_data, str):
            try:
                videos_data = json.loads(videos_data)
            except json.JSONDecodeError:
                return Response({'error': 'Invalid JSON format for videos.'}, status=status.HTTP_400_BAD_REQUEST)

        if isinstance(videos_data, dict):
            videos_data = [videos_data]

        for video_data in videos_data:
            video_id = video_data.get('video_id')
            new_video_url = video_data.get('video_url')

            if not video_id or not new_video_url:
                continue

            try:
                workshop_video = WorkshopVideo.objects.get(workshopvideo_id=video_id, workshop=workshop)
                workshop_video.video_url = new_video_url
                workshop_video.save()
            except WorkshopVideo.DoesNotExist:
                return Response({'error': f'Workshop video with ID {video_id} not found.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'workshop': workshop_serializer.data}, status=status.HTTP_200_OK)

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
class AddPageImageView(APIView):
    @transaction.atomic
    def post(self, request, page_content_id):
        try:
            page_content = PageContent.objects.get(pk=page_content_id)
        except PageContent.DoesNotExist:
            return Response({'error': 'Page content not found.'}, status=status.HTTP_404_NOT_FOUND)

        page_image = request.FILES.get('image')

        if not page_image:
            return Response({'error': 'No image file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        page_image_instance = PageImage(page=page_content, image=page_image)
        page_image_instance.save()

        return Response({
            'message': 'Page image uploaded successfully.',
            'page_image': {
                'page_image_id': page_image_instance.pageimage_id,
                'page_name': page_content.page_name,
                'image_url': page_image_instance.image.url
            }
        }, status=status.HTTP_201_CREATED)

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

# @method_decorator(csrf_exempt, name='dispatch')
# class CategoryImageDeleteView(APIView):
#     def delete(self, request, category_image_id):
#         try:
#             category_image = CategoryImage.objects.get(pk=category_image_id)
#             category_image.delete()
#             return Response({'message': 'Category image deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
#         except CategoryImage.DoesNotExist:
#             return Response({'error': 'Category image not found.'}, status=status.HTTP_404_NOT_FOUND)

# @method_decorator(csrf_exempt, name='dispatch')
# class ProductImageDeleteView(APIView):
#     def delete(self, request, product_image_id):
#         try:
#             product_image = ProductImage.objects.get(pk=product_image_id)
#             product_image.delete()
#             return Response({'message': 'Product image deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
#         except ProductImage.DoesNotExist:
#             return Response({'error': 'Product image not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class CategoryImageDeleteView(APIView):
    def delete(self, request, category_image_id):
        try:
            category_image = CategoryImage.objects.get(pk=category_image_id)
            # Manually delete the image file
            if category_image.image and default_storage.exists(category_image.image.name):
                default_storage.delete(category_image.image.name)
            # Delete the CategoryImage instance
            category_image.delete()
            return Response({'message': 'Category image deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except CategoryImage.DoesNotExist:
            return Response({'error': 'Category image not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class ProductImageDeleteView(APIView):
    def delete(self, request, product_image_id):
        try:
            product_image = ProductImage.objects.get(pk=product_image_id)
            # Manually delete the image file
            if product_image.image and default_storage.exists(product_image.image.name):
                default_storage.delete(product_image.image.name)
            # Delete the ProductImage instance
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
            # Delete the image file manually
            if banner_image.image and default_storage.exists(banner_image.image.name):
                default_storage.delete(banner_image.image.name)
            # Delete the BannerImage instance
            banner_image.delete()
            return Response({'message': 'Banner image deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except BannerImage.DoesNotExist:
            return Response({'error': 'Banner image not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class CustomerDeleteView(APIView):
    def delete(self, request, customer_id):
        try:
            customer = Customer.objects.get(pk=customer_id)
            customer.delete()
            return Response({'message': 'Customer deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class OrderDeleteView(APIView):
    def delete(self, request, order_id):
        try:
            order = Order.objects.get(pk=order_id)
            order.delete()
            return Response({'message': 'Order deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class OrderItemDeleteView(APIView):
    def delete(self, request, order_item_id):
        try:
            order_item = OrderItem.objects.get(pk=order_item_id)
            order_item.delete()
            return Response({'message': 'Order item deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except OrderItem.DoesNotExist:
            return Response({'error': 'Order item not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class PageContentDeleteView(APIView):
    def delete(self, request, page_content_id):
        try:
            page_content = PageContent.objects.get(pk=page_content_id)
            page_content.delete()  # This will also delete related PageImage entries due to on_delete=models.CASCADE
            return Response({'message': 'Page content and associated images deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except PageContent.DoesNotExist:
            return Response({'error': 'Page content not found.'}, status=status.HTTP_404_NOT_FOUND)

# @method_decorator(csrf_exempt, name='dispatch')
# class PageImageDeleteView(APIView):
#     def delete(self, request, page_content_id):
#         try:
#             page_content = PageContent.objects.get(pk=page_content_id)
#             page_images = PageImage.objects.filter(page=page_content)
#             if page_images.exists():
#                 page_images.delete()  # This will delete all images associated with the specified page content
#                 return Response({'message': 'Images for the specified page content deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
#             else:
#                 return Response({'message': 'No images found for the specified page content.'}, status=status.HTTP_404_NOT_FOUND)
#         except PageContent.DoesNotExist:
#             return Response({'error': 'Page content not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class PageImageDeleteView(APIView):
    def delete(self, request, page_content_id):
        try:
            page_content = PageContent.objects.get(pk=page_content_id)
            page_images = PageImage.objects.filter(page=page_content)
            if page_images.exists():
                # Manually delete each image file associated with the page content
                for image in page_images:
                    if image.image and default_storage.exists(image.image.name):
                        default_storage.delete(image.image.name)
                # Delete all PageImage instances for the specified page content
                page_images.delete()
                return Response({'message': 'Images for the specified page content deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message': 'No images found for the specified page content.'}, status=status.HTTP_404_NOT_FOUND)
        except PageContent.DoesNotExist:
            return Response({'error': 'Page content not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class WorkshopDeleteView(APIView):
    def delete(self, request, workshop_id):
        try:
            workshop = Workshop.objects.get(pk=workshop_id)
            workshop.delete()
            return Response({'message': 'Workshop deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Workshop.DoesNotExist:
            return Response({'error': 'Workshop not found.'}, status=status.HTTP_404_NOT_FOUND)

# @method_decorator(csrf_exempt, name='dispatch')
# class WorkshopImageDeleteView(APIView):
#     def delete(self, request, workshop_image_id):
#         try:
#             workshop_image = WorkshopImage.objects.get(pk=workshop_image_id)
#             workshop_image.delete()
#             return Response({'message': 'Workshop image deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
#         except WorkshopImage.DoesNotExist:
#             return Response({'error': 'Workshop image not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class WorkshopImageDeleteView(APIView):
    def delete(self, request, workshop_image_id):
        try:
            workshop_image = WorkshopImage.objects.get(pk=workshop_image_id)
            # Manually delete the image file
            if workshop_image.image and default_storage.exists(workshop_image.image.name):
                default_storage.delete(workshop_image.image.name)
            # Delete the WorkshopImage instance
            workshop_image.delete()
            return Response({'message': 'Workshop image deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except WorkshopImage.DoesNotExist:
            return Response({'error': 'Workshop image not found.'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class WorkshopVideoDeleteView(APIView):
    def delete(self, request, workshop_video_id):
        try:
            workshop_video = WorkshopVideo.objects.get(pk=workshop_video_id)
            workshop_video.delete()
            return Response({'message': 'Workshop video deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except WorkshopVideo.DoesNotExist:
            return Response({'error': 'Workshop video not found.'}, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def send_message_view(request):
    if request.method == 'POST':
        try:
            # Parse JSON request body
            data = json.loads(request.body.decode('utf-8'))
            message_body = data.get('message', '')
            to_number = '917353647516'  # Replace with the actual recipient number

            formatted_message = f"{message_body}"

            # Send WhatsApp message
            message_sid = send_whatsapp_message(to_number, formatted_message)
            return JsonResponse({'status': 'success', 'message_sid': message_sid})
        except Exception as e:
            return JsonResponse({'status': 'error', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'error': 'Invalid method'}, status=405)

# @method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class CreateOrderView(APIView):
    @transaction.atomic
    def post(self, request):
        try:
            # Extract customer details
            customer_data = request.data.get('customerDetails', '{}')
            order_data = request.data.get('orderDetails', '{}')
            items_data = order_data.get('items', '[]')

            # Save Customer
            customer_serializer = CustomerSerializer(data=customer_data)
            if customer_serializer.is_valid():
                customer = customer_serializer.save()
            else:
                return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Save Order
            order_data = {
                'customer': customer.customer_id,
                'total_amount': order_data['total'],
                'count': order_data['count'],
            }
            order_serializer = OrderSerializer(data=order_data)
            if order_serializer.is_valid():
                order = order_serializer.save()
            else:
                transaction.set_rollback(True)
                return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Save Order Items
            for item in items_data:
                item_data = {
                    'order': order.order_id,
                    'product': item['product_id'],
                    'quantity': item['quantity'],
                    'price': item['price'],
                }
                order_item_serializer = OrderItemSerializer(data=item_data)
                if order_item_serializer.is_valid():
                    order_item_serializer.save()
                else:
                    transaction.set_rollback(True)
                    return Response(order_item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'Order created successfully.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            transaction.set_rollback(True)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    
