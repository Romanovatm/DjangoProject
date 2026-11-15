from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
        path('', BlogListView.as_view(), name='blog_list'),
        path('create/', BlogCreateView.as_view(), name='post_create'),
        path('post_details/<int:pk>/', BlogDetailView.as_view(), name='post_details'),
        path('update/<int:pk>/', BlogUpdateView.as_view(), name='post_update'),
        path('delete/<int:pk>/', BlogDeleteView.as_view(), name='post_delete'),
]
