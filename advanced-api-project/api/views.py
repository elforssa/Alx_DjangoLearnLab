from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# ListView for retrieving all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow all users to view the list

# DetailView for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow all users to view book details

# CreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create

# UpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update

# DeleteView for removing a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author__name', 'publication_year']  # Filter by book title, author's name, and publication year
    filters.SearchFilter = ['title', 'author__name']  # Search by book title or author'
    ordering_fields = ['title', 'publication_year']  # Allow
    
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Set up data for tests
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='J.R.R. Tolkien')
        self.book1 = Book.objects.create(title='The Hobbit', publication_year=1937, author=self.author)
        self.book2 = Book.objects.create(title='The Lord of the Rings', publication_year=1954, author=self.author)
        self.client = APIClient()

    def test_create_book(self):
        # Log in as a user
        self.client.login(username='testuser', password='testpassword')

        # Create a new book
        url = reverse('book-list')  # Assuming 'book-list' is defined in your urls
        data = {
            'title': 'The Silmarillion',
            'publication_year': 1977,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=3).title, 'The Silmarillion')

    def test_retrieve_book(self):
        # Test retrieving an existing book
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'The Hobbit')

    def test_update_book(self):
        # Log in as a user and update a book
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-detail', args=[self.book1.id])
        data = {'title': 'The Hobbit: Revised Edition', 'publication_year': 1937, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'The Hobbit: Revised Edition')

    def test_delete_book(self):
        # Log in as a user and delete a book
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        # Test filtering by title
        url = reverse('book-list') + '?title=The Hobbit'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')

    def test_search_books(self):
        # Test searching for books by title
        url = reverse('book-list') + '?search=Rings'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Lord of the Rings')

    def test_order_books(self):
        # Test ordering books by publication_year
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')  # Oldest book first

    def test_permissions(self):
        # Test that non-authenticated users cannot create a book
        url = reverse('book-list')
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
