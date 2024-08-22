
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
from django.contrib.auth import login

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

UserCreationForm()", "relationship_app/register.html

from .models import Library

# relationship_app/views.py

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Role check functions
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Admin View (restricted to Admin role)
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# Librarian View (restricted to Librarian role)
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Member View (restricted to Member role)
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
