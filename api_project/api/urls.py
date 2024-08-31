from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'books', BookViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]
