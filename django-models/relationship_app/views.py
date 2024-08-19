from django.shortcuts import render

# Create your views here.
from .models import Book

def list_books(request):
    books = Book.objects.all()
    # Create a simple text list of books and their authors
    book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(book_list, content_type="text/plain")

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

