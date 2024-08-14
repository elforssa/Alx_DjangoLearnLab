# Create Operation

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected output: Book instance created with ID <ID> (replace <ID> with the actual ID)
