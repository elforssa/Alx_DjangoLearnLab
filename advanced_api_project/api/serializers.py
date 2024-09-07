from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer serializes the Book model and includes validation to ensure the
    publication year is not set in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        if value > timezone.now().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer serializes the Author model and includes a nested BookSerializer
    to represent the related books.
    """
    books = BookSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

