# Retrieve Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title)  # Expected output: "1984"
print(book.author)  # Expected output: "George Orwell"
print(book.publication_year)  # Expected output: 1949
