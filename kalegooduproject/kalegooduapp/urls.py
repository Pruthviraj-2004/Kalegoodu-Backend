from django import views
from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ProductImageViewSet, CategoryImageViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'category-images', CategoryImageViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', include(router.urls)),
]
