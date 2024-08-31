from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use the BookSerializer to convert Book objects to JSON

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting book instances.
    """
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer for serialization
