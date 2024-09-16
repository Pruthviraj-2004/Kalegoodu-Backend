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
    path('customers/', CustomerView.as_view(), name='customer-list'),
    path('orders/', OrderView.as_view(), name='order-list'),
    path('order-items/', OrderItemView.as_view(), name='order-item-list'),
    path('page-contents/', PageContentListView.as_view(), name='page-content-list'),
    path('page-images/', PageImageListView.as_view(), name='page-image-list'),
    path('workshops/', WorkshopListView.as_view(), name='workshop-list'),
    path('workshop-images/', WorkshopImageListView.as_view(), name='workshop-image-list'),
    path('workshop-videos/', WorkshopVideoListView.as_view(), name='workshop-video-list'),

    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('sale_types/<int:sale_type_id>/', SaleTypeDetailAPIView.as_view(), name='sale-type-detail'),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('product_images/<int:product_image_id>/', ProductImageDetailAPIView.as_view(), name='product-image-detail'),
    path('category_images/<int:category_image_id>/', CategoryImageDetailAPIView.as_view(), name='category-image-detail'),
    path('comments/<int:comment_id>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    path('banner_images/', BannerImageView.as_view(), name='banner_image_create'),
    path('orders/<int:order_id>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('customers/<int:customer_id>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
    path('page-contents/<int:pagecontent_id>/', PageContentDetailView.as_view(), name='page-content-detail'),
    path('page-images/<int:pageimage_id>/', PageImageDetailView.as_view(), name='page-image-detail'),
    path('workshops/<int:workshop_id>/', WorkshopDetailView.as_view(), name='workshop-detail'),
    path('workshop-images/<int:workshop_image_id>/', WorkshopImageDetailView.as_view(), name='workshop-image-detail'),
    path('workshop-videos/<int:workshop_video_id>/', WorkshopVideoDetailView.as_view(), name='workshop-video-detail'),

    path('products_by_category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products-by-category'),
    path('categories_by_product/<int:product_id>/', CategoriesByProduct.as_view(), name='categories_by_product'),
    path('orders_details_customer/<int:order_id>/', OrderDetailWithCustomerAPIView.as_view(), name='order-detail-with-customer'),

    path('add_category/', CategoryCreateView.as_view(), name='category_create'),#add with images
    path('add_product/', ProductCreateView.as_view(), name='product_create'),#add with images
    path('add_category_image/<int:category_id>/', AddCategoryImageView.as_view(), name='add_category_image'),
    path('add_product_image/<int:product_id>/', AddProductImageView.as_view(), name='add_product_image'),
    path('add_page_contents/', PageContentCreateView.as_view(), name='page-content-create'),
    path('add_page_image/<int:page_content_id>/', AddPageImageView.as_view(), name='add-page-image'),

    path('update_category/<int:category_id>/', CategoryUpdateView.as_view(), name='category_update'),
    path('update_category_image/<int:image_id>/', CategoryImageUpdateView.as_view(), name='category_image_update'),
    path('update_full_category/<int:category_id>/', FullCategoryUpdateView.as_view(), name='category_update'),
    path('update_product/<int:product_id>/', ProductUpdateView.as_view(), name='product_update'),
    path('update_product_image/<int:image_id>/', ProductImageUpdateView.as_view(), name='product_image_update'),
    path('update_full_product/<int:product_id>/', ProductFullUpdateView.as_view(), name='product_full_update'),
    path('update_sale_type/<int:sale_type_id>/', SaleTypeUpdateView.as_view(), name='sale_type_update'),
    path('update_comment/<int:comment_id>/', CommentUpdateView.as_view(), name='comment_update'),
    path('update_banner_image/<int:banner_image_id>/', BannerImageUpdateView.as_view(), name='banner_image_update'),
    path('update_customers/<int:customer_id>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('update_orders/<int:order_id>/', OrderUpdateView.as_view(), name='order-update'),
    path('update_order_items/<int:order_item_id>/', OrderItemUpdateView.as_view(), name='order-item-update'),
    path('update_page_contents/<int:page_content_id>/', FullPageContentUpdateView.as_view(), name='page-content-update'),
    path('update_workshops/<int:workshop_id>/', WorkshopUpdateView.as_view(), name='workshop-update'),


    path('sale_type/<int:sale_type_id>/delete/', SaleTypeDeleteView.as_view(), name='sale-type-delete'),
    path('category/<int:category_id>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('product/<int:product_id>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('category_image/<int:category_image_id>/delete/', CategoryImageDeleteView.as_view(), name='category-image-delete'),
    path('product_image/<int:product_image_id>/delete/', ProductImageDeleteView.as_view(), name='product-image-delete'),
    path('comment/<int:comment_id>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('banner_image/<int:banner_image_id>/delete/', BannerImageDeleteView.as_view(), name='banner-image-delete'),
    path('customers/<int:customer_id>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
    path('orders/<int:order_id>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    path('order-items/<int:order_item_id>/delete/', OrderItemDeleteView.as_view(), name='order-item-delete'),
    path('page-contents/delete/<int:page_content_id>/', PageContentDeleteView.as_view(), name='page-content-delete'),
    path('page-images/delete/<int:page_content_id>/', PageImageDeleteView.as_view(), name='page-image-delete'),
    path('workshops/<int:workshop_id>/delete/', WorkshopDeleteView.as_view(), name='workshop-delete'),
    path('workshop-images/<int:workshop_image_id>/delete/', WorkshopImageDeleteView.as_view(), name='workshop-image-delete'),
    path('workshop-videos/<int:workshop_video_id>/delete/', WorkshopVideoDeleteView.as_view(), name='workshop-video-delete'),


    path('send-message/', send_message_view, name='send_message'),
    path('create-order/', CreateOrderView.as_view(), name='create-order'),
    path('acknowledge_order/', UpdateOrderView.as_view(), name='acknowledge-order'),
    path('workshops-create/', WorkshopCreateView.as_view(), name='workshop-create'),


    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),




]