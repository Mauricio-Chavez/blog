from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post
    # context_object_name = 'posts'

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post
    # context_object_name = 'post'

class PostCreateView(CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = ['title','subtitle','author','body','status']

class PostUpdateView(UpdateView):
    template_name = 'posts/edit.html'
    model = Post
    fields = ['title','subtitle','body','status']

class PostDeleteView(DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('list')

class HomePageView(TemplateView):
    template_name = "pages/home.html"
    
class AboutPageView(TemplateView):
    template_name = "pages/about.html"