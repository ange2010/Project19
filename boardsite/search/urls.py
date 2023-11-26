from django.urls import path

from search.views import SearchItems, SearchCategories

urlpatterns = [
    path('item/<str:query>/', SearchItems.as_view()),
    path('category/<str:query>/', SearchCategories.as_view()),
]
