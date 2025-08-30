# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RegisterForm, PostForm
from .models import Post, Comment
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag  # from django-taggit



# --------------------------
# Authentication Views
# --------------------------

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to home page
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('post_list')  # Redirect to your posts list view
        else:
            error = "Invalid username or password"
            return render(request, 'blog/login.html', {'error': error})
    return render(request, 'blog/login.html')
           
    
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        request.user.email = email
        request.user.save()
    return render(request, 'blog/profile.html')

# --------------------------
# Home / Blog Views
# --------------------------

# Make the PostListView act as home page


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'  # Redirect to home page after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    



from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import CommentForm

# Display post details and comments, handle new comment submissions
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include a blank comment form in the template context
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        # Handles POST requests (when a user submits a comment)
        self.object = self.get_object()  # Get the current post
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.post = self.object  # Associate comment with this post
            comment.author = request.user  # Set the comment author
            comment.save()  # Save to database
            return redirect('post_detail', pk=self.object.pk)
        # If form invalid, re-render page with form errors
        context = self.get_context_data(comment_form=form)
        return self.render_to_response(context)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    # Ensure only the author can edit
    def test_func(self):
        return self.request.user == self.get_object().author

    # Redirect back to post after editing
    def get_success_url(self):
        return self.object.post.get_absolute_url()



class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    # Ensure only the author can delete
    def test_func(self):
        return self.request.user == self.get_object().author

    # Redirect back to post after deleting
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_id']})
    




from django.db.models import Q  # Q objects allow complex queries

def search_view(request):
    """
    Handles search functionality.
    - Gets the query string from GET parameters.
    - Filters posts by title, content, or associated tags.
    - Passes the results to the search_results template.
    """
    query = request.GET.get('q')  # Retrieve search keyword
    results = Post.objects.none()  # Initialize empty queryset
    if query:
        # Search title, content, and tags (case-insensitive)
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()  # Avoid duplicates if multiple tags match
    return render(request, 'blog/search_results.html', {'query': query, 'results': results})


# ... keep your existing imports and views (PostListView, PostDetailView, etc.)

def search(request):
    """
    Search posts by title, content, or tag names.
    URL: /search/?q=term
    """
    query = request.GET.get('q', '').strip()
    results = Post.objects.none()

    if query:
        results = (
            Post.objects
            .filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)  # ✅ search by tag name
            )
            .distinct()
            .order_by('-published_date')
        )

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'blog/search_results.html', context)

def posts_by_tag(request, tag_slug):
    """
    List posts that have a specific tag.
    URL: /tags/<tag_slug>/
    """
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__in=[tag]).order_by('-published_date')
    context = {
        'tag': tag,
        'posts': posts,
    }
    return render(request, 'blog/posts_by_tag.html', context)
