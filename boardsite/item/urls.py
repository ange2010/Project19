from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('item_view/', views.ItemViewSet.as_view({'get': 'list'}), name='item_view'),
    path('category_view/', views.CategoryViewSet.as_view({'get': 'list'}), name='category_view'),
]
