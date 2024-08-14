# Delete Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Attempt to retrieve the deleted book
try:
    Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("Book successfully deleted.")  # Expected output: "Book successfully deleted."
