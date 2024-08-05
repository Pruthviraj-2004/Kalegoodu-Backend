from django import views
from django.urls import path, include
from . import views

from .views import *


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('home/', views.home, name='home'),
    path('categories/', CategoryView.as_view(), name='category-list'),
    path('sale_types/', SaleTypeView.as_view(), name='sale-type-list'),
    path('products/', ProductView.as_view(), name='product-list'),
    path('product_images/', ProductImageView.as_view(), name='product-image-list'),
    path('category_images/', CategoryImageView.as_view(), name='category-image-list'),
    path('comments/', CommentView.as_view(), name='comment-list'),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('sale_types/<int:sale_type_id>/', SaleTypeDetailAPIView.as_view(), name='sale-type-detail'),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('product_images/<int:product_image_id>/', ProductImageDetailAPIView.as_view(), name='product-image-detail'),
    path('category_images/<int:category_image_id>/', CategoryImageDetailAPIView.as_view(), name='category-image-detail'),
    path('comments/<int:comment_id>/', CommentDetailAPIView.as_view(), name='comment-detail'),

    path('add_category/', CategoryCreateView.as_view(), name='category_create'),#add with images
    path('add_product/', ProductCreateView.as_view(), name='product_create'),#add with images

]
