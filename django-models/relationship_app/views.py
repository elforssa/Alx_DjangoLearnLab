from django.shortcuts import render

# Create your views here.
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
