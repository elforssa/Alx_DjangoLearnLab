from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Redirect to the profile page after login
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

# Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})

# Extend to allow profile editing
@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'blog/edit_profile.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# ListView: Display all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # <app_name>/<model_name>_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # Order posts by newest first

# DetailView: Display an individual post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# CreateView: Allow authenticated users to create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)

# UpdateView: Allow authors to update their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can edit the post

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# DeleteView: Allow authors to delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


from django.contrib.auth.mixins import LoginRequiredMixin

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)

from django.contrib.auth.mixins import UserPassesTestMixin

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can edit the post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can delete the post

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'form': form, 'comments': comments})

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    if request.method == 'POST':
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_pk)
    return render(request, 'confirm_delete.html', {'comment': comment})
