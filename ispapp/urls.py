from django.urls import path
from .views import index, package_list, blog_list_view, blog_detail_view

urlpatterns = [
    path('', index, name='my_index'),
    path('packages/', package_list, name='package_list'),
    path('blogs/', blog_list_view, name='blogs'),
    path('blogs/<int:pk>/', blog_detail_view, name='blog_detail'),
]