from django.urls import path

from products.api_endpoints import *




urlpatterns = [
    path('list1/', ProductListAPIView1.as_view(), name="product-list1"),
    path('list2/', ProductListAPIView2.as_view(), name="product-list2"),
    path('list3/', ProductListAPIView3.as_view(), name="product-list3"),
    path('brand-create/', BrandCreateAPIView.as_view(), name="product-brand-create"),
    path('brand-list/', BrandListAPIView.as_view(), name="product-brand-list"),
    path('brand/<int:pk>/update/', BrandUpdateAPIView.as_view(), name="product-brand-update"),
    path('brand/<int:pk>/delete/', BrandDeleteAPIView.as_view(), name="product-brand-delete"),
    path('category-create/', CategoryCreateAPIView.as_view(), name="product-category-create"),
    path('category-list/', CategoryListAPIView.as_view(), name="product-category-list"),
    path('category/<int:pk>/update/', CategoryUpdateAPIView.as_view(), name="product-category-update"),
    path('category/<int:pk>/delete/', CategoryDeleteAPIView.as_view(), name="product-category-delete"),
    path('color-create/', ColorCreateAPIView.as_view(), name="product-color-create"),
    path('color-list/', ColorListAPIView.as_view(), name="product-color-list"),
    path('color/<int:pk>/update/', ColorUpdateAPIView.as_view(), name="product-color-update"),
    path('color/<int:pk>/delete/', ColorCreateAPIView.as_view(), name="product-color-delete"),
    path('mediafile-create/', MediaFileCreateAPIView.as_view(), name="product-mediafile-create"),
    path('mediafile-list/', MediaFileListAPIView.as_view(), name="product-mediafile-list"),
    path('mediafile/<int:pk>/update/', MediaFileDestroyAPIView.as_view(), name="product-mediafile-update"),
    path('mediafile/<int:pk>/delete/', MediaFileDeleteAPIView.as_view(), name="product-mediafile-delete"),
    path('productvariants-create/', ProductVariantCreateAPIView.as_view(), name="productvariants-create"),
    path('productvariants-list/', ProductVariantListAPIView.as_view(), name="productvariants-list"),
    path('productvariants/<int:pk>/update/', ProductVariantUpdateAPIView.as_view(), name="productvariants-update"),
    path('productvariants/<int:pk>/delete/', ProductVariantDeleteAPIView.as_view(), name="productvariants-delete"),
    path('size-create/', SizeCreateAPIView.as_view(), name="product-size-create"),
    path('size-list/', SizeListAPIView.as_view(), name="product-size-list"),
    path('size/<int:pk>/update/', SizeUpdateAPIView.as_view(), name="product-size-update"),
    path('size/<int:pk>/delete/', SizeDeleteAPIView.as_view(), name="product-size-delete"),
 ]   