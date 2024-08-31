from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # Include the relationship_app URLs
]

# relationship_app/urls.py

from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]

views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=
                                                                         
                                                                         
from .views import list_books

# relationship_app/urls.py

from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),
]
# relationship_app/urls.py

from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),
]

# relationship_app/urls.py

from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('add-book/', add_book, name='add_book'),
    path('edit-book/<int:pk>/', edit_book, name='edit_book'),
    path('delete-book/<int:pk>/', delete_book, name='delete_book'),
]

"add_book/", "edit_book/"