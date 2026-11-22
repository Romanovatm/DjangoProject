from django.urls import path
from .views import ProductListView, ContactView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
        path('', ProductListView.as_view(), name='home'),
        path('contacts/', ContactView.as_view(), name='contacts'),
        path('product_details/<int:product_id>/', ProductDetailView.as_view(), name='product_details'),
]
