from django import views
from django.urls import path, include
from . import views

from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('home/', views.home, name='home'),

    path('categories/', CategoryView.as_view(), name='category-list'),
    path('visible-categories/', VisibleCategoryView.as_view(), name='visible-category-list'),
    path('sale_types/', SaleTypeView.as_view(), name='sale-type-list'),
    path('products/', ProductView.as_view(), name='product-list'),
    path('list_products/', ListProductView.as_view(), name='list-product'),
    path('allcomments/', AllCommentView.as_view(), name='all-comment-list'),
    path('comments/', CommentView.as_view(), name='comment-list'),
    path('customers/', CustomerView.as_view(), name='customer-list'),#Check later
    path('list-orders/', ListOrderView.as_view(), name='list-order'),
    path('orders/', OrderView.as_view(), name='order-list'),
    path('orders/<int:order_id>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('page-contents/', PageContentListView.as_view(), name='page-content-list'),
    path('page-contents/<int:pagecontent_id>/', PageContentDetailView.as_view(), name='page-content-detail'),
    path('page-images/<int:pageimage_id>/', PageImageDetailView.as_view(), name='page-image-detail'),
    path('products-product-id/', ProductProductIdView.as_view(), name='product-list'),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('comments/<int:comment_id>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    path('banner_images/', BannerImageView.as_view(), name='banner_image_create'),
    path('customers/<int:customer_id>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
    path('workshops/', WorkshopListView.as_view(), name='workshop-list'),
    path('workshops/<int:workshop_id>/', WorkshopDetailView.as_view(), name='workshop-detail'),
    path('workshop-images/<int:workshop_image_id>/', WorkshopImageDetailView.as_view(), name='workshop-image-detail'),
    path('workshop-videos/<int:workshop_video_id>/', WorkshopVideoDetailView.as_view(), name='workshop-video-detail'),
    path('list-subcategories/', ListSubCategoryView.as_view(), name='list-subcategories'),
    path('subcategory/<int:subcategory_id>/', SubCategoryDetailView.as_view(), name='subcategory-detail'),
    path('navbar/categories/', NavbarCategoryAndSubcategoryView.as_view(), name='navbar-categories'),


    path('products_by_category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products-by-category'),
    path('orders_details_customer/<int:order_id>/', OrderDetailWithCustomerAPIView.as_view(), name='order-detail-with-customer'),
    path('products_by_saletype/<int:sale_type_id>/', ProductsBySaleTypeView.as_view(), name='products-by-saletype'),
    path('subcategories_by_category/<int:category_id>/', SubCategoryListByCategoryView.as_view(), name='subcategories-by-category'),
    path('subcategories_by_categories/', SubCategoryListByCategoriesView.as_view(), name='subcategories-by-categories'),
    path('products_by_subcategory/<int:subcategory_id>/', ProductsBySubCategoryView.as_view(), name='products-by-subcategory'),
    path('new_products_by_category/<int:category_id>/', ProductsGroupedBySubCategoryView.as_view(), name='products-by-category'),


    path('add_category/', CategoryCreateView.as_view(), name='category_create'),#add with images
    path('add_product/', ProductCreateView.as_view(), name='product_create'),#add with images
    path('add_category_image/<int:category_id>/', AddCategoryImageView.as_view(), name='add_category_image'),
    path('add_product_image/<int:product_id>/', AddProductImageView.as_view(), name='add_product_image'),
    path('add_page_contents/', PageContentCreateView.as_view(), name='page-content-create'),
    path('add_page_image/<int:page_content_id>/', AddPageImageView.as_view(), name='add-page-image'),
    path('add_subcategory/', SubCategoryCreateView.as_view(), name='add-subcategory'),
    path('add_subcategory_image/<int:subcategory_id>/', AddSubCategoryImageView.as_view(), name='add-subcategory-image'),
    path('add_workshop/', WorkshopCreateView.as_view(), name='workshop-create'),
    path('workshops/<int:workshop_id>/add-images/', WorkshopImageView.as_view(), name='workshop-add-images'),
    path('workshops/<int:workshop_id>/add-videos/', WorkshopVideoView.as_view(), name='workshop-add-videos'),


    path('update_category/<int:category_id>/', CategoryUpdateView.as_view(), name='category_update'),
    path('update_category_image/<int:image_id>/', CategoryImageUpdateView.as_view(), name='category_image_update'),
    path('update_product/<int:product_id>/', ProductUpdateView.as_view(), name='product_update'),
    path('update_product_image/<int:image_id>/', ProductImageUpdateView.as_view(), name='product_image_update'),
    path('update_sale_type/<int:sale_type_id>/', SaleTypeUpdateView.as_view(), name='sale_type_update'),
    path('update_comment/<int:comment_id>/', CommentUpdateView.as_view(), name='comment_update'),
    path('update_banner_image/<int:banner_image_id>/', BannerImageUpdateView.as_view(), name='banner_image_update'),
    path('update_customers/<int:customer_id>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('update_orders/<int:order_id>/', OrderUpdateView.as_view(), name='order-update'),
    path('update_order_items/<int:order_item_id>/', OrderItemUpdateView.as_view(), name='order-item-update'),
    path('update_page_contents/<int:page_content_id>/', FullPageContentUpdateView.as_view(), name='page-content-update'),
    path('update_workshops/<int:workshop_id>/', WorkshopUpdateView.as_view(), name='workshop-update'),
    path('update_workshop_image/<int:image_id>/', WorkshopImageUpdateView.as_view(), name='workshop-image-update'),
    path('update_subcategory/<int:subcategory_id>/', SubCategoryUpdateView.as_view(), name='update-subcategory'),
    path('update_subcategory_image/<int:image_id>/', SubCategoryImageUpdateView.as_view(), name='update-subcategory-image'),
    path('page-images/<int:pageimage_id>/', PageImageUpdateView.as_view(), name='update_page_image'),


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
    path('subcategory/<int:subcategory_id>/delete/', SubCategoryDeleteView.as_view(), name='delete-subcategory'),
    path('subcategory_image/<int:subcategory_image_id>/delete/', SubCategoryImageDeleteView.as_view(), name='delete-subcategory-image'),



    # path('send-message/', send_message_view, name='send_message'),
    path('create-order/', CreateOrderView.as_view(), name='create-order'),
    path('acknowledge_order/', UpdateOrderView.as_view(), name='acknowledge-order'),
    path('validate-stock/', ValidateStockView.as_view(), name='validate-stock'),


    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('export-customers-orders/', ExportCustomersOrdersView.as_view(), name='export-customers-orders'),
    path('export-customers-orders-by-date/', ExportCustomersOrdersByDateView.as_view(), name='export_customers_orders_by_date'),


    path('create-payment/', create_order, name='create-payment'),
    path('verify-payment/', paymenthandler, name='verify-payment'),


    path('send-promotional-emails/', SendProductPromotionalEmails.as_view(), name='send_promotional_emails'),
    path('send-workshop-promotional-emails/', SendWorkshopPromotionEmails.as_view(), name='send_workshop_promotional_emails'),
    path('unsubscribe/<str:email>/', UnsubscribeView.as_view(), name='unsubscribe'),


]
