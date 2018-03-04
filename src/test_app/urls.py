from django.urls import path
from . views import ProductCreateView
from . views import ProductDeleteView
from . views import ProductDetailView
from . views import ProductListView

app_name = 'test_app'
urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/detail/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
