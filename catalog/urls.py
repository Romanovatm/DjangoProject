from django.urls import path
from .views import ProductListView, ContactView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductCreateView

app_name = 'catalog'

urlpatterns = [
        path('', ProductListView.as_view(), name='home'),
        path('contacts/', ContactView.as_view(), name='contacts'),
        path('product_details/<int:product_id>/', ProductDetailView.as_view(), name='product_details'),
        path('product_update/<int:product_id>/', ProductUpdateView.as_view(), name='product_update'),
        path('product_delete/<int:product_id>/', ProductDeleteView.as_view(), name='product_delete'),
        path('create/', ProductCreateView.as_view(), name='product_create'),
]
