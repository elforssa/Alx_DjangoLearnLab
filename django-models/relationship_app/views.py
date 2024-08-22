
# relationship_app/views.py

from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'




# relationship_app/views.py

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Login View
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Logout View
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

# Registration View
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')  # Redirect to login after registration
