from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post
    # context_object_name = 'posts'

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post
    # context_object_name = 'post'

class PostCreateView(LoginRequiredMixin,CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = ['title','subtitle','body','status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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