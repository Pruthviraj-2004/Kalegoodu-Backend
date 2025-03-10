from django.contrib import admin
from .models import BannerImage, Category, Customer, Order, OrderItem, PageContent, PageImage, Product, ProductImage, CategoryImage, Comment, SaleType, SubCategory, SubCategoryImage, Workshop, WorkshopImage, WorkshopVideo
from import_export.admin import ImportExportModelAdmin
from .resources import (CustomerResource, OrderItemResource, OrderResource, SaleTypeResource,CategoryResource,ProductResource,CategoryImageResource,ProductImageResource,CommentResource,BannerImageResource)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 1

class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('product_id', 'name', 'price', 'quantity', 'discounted_price', 
                    'get_categories', 'get_subcategories', 'get_sale_types', 
                    'video_link', 'visible', 'created_at', 'updated_at')
    list_filter = ('categories', 'subcategories', 'sale_types', 'visible')
    search_fields = ('name', 'categories__name', 'subcategories__name', 'sale_types__name')
    inlines = [ProductImageInline]

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'

    def get_subcategories(self, obj):
        return ", ".join([subcategory.name for subcategory in obj.subcategories.all()])
    get_subcategories.short_description = 'Subcategories'

    def get_sale_types(self, obj):
        return ", ".join([sale_type.name for sale_type in obj.sale_types.all()])
    get_sale_types.short_description = 'Sale Types'

admin.site.register(Product, ProductAdmin)

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ('category_id', 'name', 'description', 'visible', 'header', 'home_page', 'created_at', 'updated_at')
    inlines = [CategoryImageInline]

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    resource_class = CommentResource
    list_display = ('comment_id', 'product', 'user_name', 'text', 'display','created_at', 'updated_at')
    list_filter = ('product', 'created_at')
    search_fields = ('user_name', 'product__name')

@admin.register(ProductImage)
class ProductImageAdmin(ImportExportModelAdmin):
    resource_class = ProductImageResource
    list_display = ('product_image_id', 'product', 'image', 'visible', 'alt_text', 'created_at', 'updated_at')

@admin.register(CategoryImage)
class CategoryImageAdmin(ImportExportModelAdmin):
    resource_class = CategoryImageResource
    list_display = ('category_image_id', 'category', 'image', 'visible', 'alt_text', 'created_at', 'updated_at')

@admin.register(SaleType)
class SaleTypeAdmin(ImportExportModelAdmin):
    resource_class = SaleTypeResource
    list_display = ('sale_type_id', 'name', 'visible')
    search_fields = ('name',)

@admin.register(BannerImage)
class BannerImageAdmin(ImportExportModelAdmin):
    resource_class = BannerImageResource
    list_display = ('banner_image_id', 'title', 'image', 'visible', 'created_at', 'updated_at')
    search_fields = ('title',)

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource
    list_display = ('customer_id', 'name', 'phone_number', 'email', 'address', 'pincode', 'visible', 'send_promotion_emails', 'created_at', 'updated_at')
    search_fields = ('customer_id', 'name', 'phone_number', 'email', 'pincode')

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    resource_class = OrderResource
    list_display = ('order_id', 'customer', 'count', 'total_amount', 'order_completed', 'visible', 'note','created_at', 'updated_at')

@admin.register(OrderItem)
class OrderItemAdmin(ImportExportModelAdmin):
    resource_class = OrderItemResource
    list_display = ('order_item_id', 'order', 'product', 'quantity', 'price', 'order_completed', 'visible', 'created_at', 'updated_at')

class PageImageInline(admin.TabularInline):
    model = PageImage

class PageContentAdmin(admin.ModelAdmin):
    list_display = ('pagecontent_id', 'page_name', 'visible', 'created_at', 'updated_at')
    inlines = [PageImageInline]

admin.site.register(PageContent, PageContentAdmin)
admin.site.register(PageImage)

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('workshop_id', 'name','date', 'place', 'completed')

@admin.register(WorkshopImage)
class WorkshopImageAdmin(admin.ModelAdmin):
    list_display = ('workshopimage_id', 'workshop', 'image', 'visible')

@admin.register(WorkshopVideo)
class WorkshopVideoAdmin(admin.ModelAdmin):
    list_display = ('workshopvideo_id', 'workshop', 'video_url', 'visible')

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory_id', 'name', 'get_categories', 'visible', 'header', 'category_page', 'created_at', 'updated_at')
    list_filter = ('category', 'visible', 'header', 'category_page')
    search_fields = ('name', 'category__name')

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])

    get_categories.short_description = "Categories"

@admin.register(SubCategoryImage)
class SubCategoryImageAdmin(admin.ModelAdmin):
    list_display = ('subcategory_image_id', 'subcategory', 'visible', 'created_at', 'updated_at')
    list_filter = ('subcategory', 'visible')
